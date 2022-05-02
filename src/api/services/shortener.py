import validators
from src.api.models.bitly_shortener import Bitly_Shortener

from src.exceptions.validation import Invalid_Type, Invalid_Url, Missing_Property
from src.helpers.providers import Shortening_Providers


class Shortener_Service():

    # Checks if the provider given is a valid one and is supported
    def is_valid_provider(self, provider):
        if provider in Shortening_Providers.__members__:
            return True

        return False

    # Bussines logic for bitly API shortening url provider
    def shorten_url_bitly(self, payload):
        # Sanitize data, check their validity
        if not 'url' in payload:
            raise Missing_Property(property='url')

        if not isinstance(payload['url'], str):
            raise Invalid_Type(property='url')

        if not validators.url(payload['url']):
            raise Invalid_Url()

        _model = Bitly_Shortener(
            url=payload['url'], 
            provider=payload['provider'])
        shortened_url = _model.shorten_url()

        return {'url': payload['url'], 'link': shortened_url, 'http_code': 200}

    # Bussines logic for tinyurl API shortening url provider
    def shorten_url_tinyurl(self, payload):
        # Sanitize data, check their validity
        if not 'url' in payload:
            raise Missing_Property(property='url')

        if not isinstance(payload['url'], str):
            raise Invalid_Type(property='url')

        if not validators.url(payload['url']):
            raise Invalid_Url()

        # TODO: call appropriate model

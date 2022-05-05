import validators
from src.api.models.tinyurl_shortener import Tinyurl_Shortener
from src.api.models.bitly_shortener import Bitly_Shortener

from src.exceptions.validation import Invalid_Type, Invalid_Url, Missing_Property
from src.helpers.providers import Shortening_Providers


class Shortener_Service():
    """ Services class part of the bussines layer of the application that contains
        all the necessary services for the shortening domain. Services are responsible
        for validating the input given from the request, sanitizing it and calling the
        appropriate Model class method(-s) that will then shorten the url.
    """

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

        return shortened_url

    # Bussines logic for tinyurl API shortening url provider
    def shorten_url_tinyurl(self, payload):
        # Sanitize data, check their validity
        if not 'url' in payload:
            raise Missing_Property(property='url')

        if not isinstance(payload['url'], str):
            raise Invalid_Type(property='url')

        if not validators.url(payload['url']):
            raise Invalid_Url()

        _model = Tinyurl_Shortener(
            url=payload['url'],
            provider=payload['provider'])
        shortened_url = _model.shorten_url()

        return shortened_url

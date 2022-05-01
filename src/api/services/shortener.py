import validators

from src.exceptions.validation import Invalid_Type, Invalid_Url, Missing_Property


class Shortener_Service():

    def is_valid_provider(self, provider):
        provider = provider.lower()
        if provider == 'bitly' or provider == 'tinyurl':
            return True
        return False

    def shorten_url_bitly(self, payload):
        # Sanitize data, check their validity
        if not 'url' in payload:
            raise Missing_Property(property='url')

        if not isinstance(payload['url'], str):
            raise Invalid_Type(property='url')

        if not validators.domain(payload['url']):
            raise Invalid_Url()

        # TODO: call appropriate model

    def shorten_url_tinyurl(self, payload):
        # Sanitize data, check their validity
        if not 'url' in payload:
            raise Missing_Property(property='url')

        if not isinstance(payload['url'], str):
            raise Invalid_Type(property='url')

        if not validators.domain(payload['url']):
            raise Invalid_Url()

        # TODO: call appropriate model

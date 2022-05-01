import validators

from src.exceptions.validation import MissingProperty

class Shortener_Service():

    def shorten_url_bitly(self, payload):
        try:
            # Sanitize data, check their validity
            if not 'url' in payload:
                raise MissingProperty(property='url')

            if not isinstance(payload['url'], str):
                raise Exception("No a string")

            if not validators.domain(payload['url']):
                raise Exception("No a valid url")


            # TODO: call appropriate model

        except Exception as ex:
            print(ex)
            print("An exception occurred")

    def shorten_url_tinyurl(self, payload):
        try:
            # Sanitize data, check their validity
            if not payload['url']:
                raise Exception("No url provided")

            if not isinstance(payload['url'], str):
                raise Exception("No a string")

            if not validators.domain(payload['url']):
                raise Exception("No a valid url")


            # TODO: call appropriate model

        except:
            print("An exception occurred")

from flask import request, jsonify
from src.api.services.shortener import Shortener_Service
from src.exceptions.validation import Invalid_Api_Provider


class Shortener_Controller():

    def __init__(self):
        self._service = Shortener_Service()

    def shorten_url(self):
        try:
            payload = request.json
            provider = provider.lower()

            # Check if the provider given is valid
            if not self._service.is_valid_provider(provider):
                raise Invalid_Api_Provider()

            # if provider == 'bitly':
            #     response = self._service.shorten_url_bitly(payload)
            # elif provider == 'tinyurl':
            #     response = self._service.shorten_url_tinyurl(payload)

            return jsonify(response)

        except Exception as ex:
            return jsonify(ex)



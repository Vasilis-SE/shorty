from flask import request, jsonify
from src.api.controllers.base_controller import Base_Controller
from src.api.services.shortener import Shortener_Service
from src.exceptions.validation import Invalid_Api_Provider
from src.helpers.providers import Shortening_Providers


class Shortener_Controller(Base_Controller):

    def __init__(self):
        self._service = Shortener_Service()

    def shorten_url(self):
        try:
            payload = request.json
            provider = payload['provider'].upper() if 'provider' in payload else ''

            # Check if the provider given is valid
            if not self._service.is_valid_provider(provider):
                raise Invalid_Api_Provider()

            shortening_func = getattr(self._service, Shortening_Providers[payload['provider'].upper()].value)
            response = shortening_func(payload)

            return self.send(response)
        except Exception as ex:
            return self.send(ex.__dict__)

from flask import request
from src.exceptions.shortener import Shortening_Failed
from src.helpers.http_codes import HTTP_Codes
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

            # If no provider property is passed then set the default shortener (tinyurl)
            provider = payload['provider'].upper(
            ) if 'provider' in payload else 'TINYURL'
            providers_list = [el.name for el in Shortening_Providers]

            # If there is a provider property but its not on the list throw Invalid_Api_Provider exception
            if not self._service.is_valid_provider(provider):
                raise Invalid_Api_Provider()

            providers_list.pop(providers_list.index(provider))

            # If there is a provider & is valid call the appropriate service from the enum name
            shortened_url = False
            while not shortened_url or len(providers_list) != 0:
                shortening_func = getattr(
                    self._service,
                    Shortening_Providers[provider].value)
                shortened_url = shortening_func(payload)

                # print(provider + ": " + str(shortened_url))
                if len(providers_list) > 0:
                    provider = providers_list.pop(0)

            if not shortened_url:
                raise Shortening_Failed()

            response = {
                'url': payload['url'],
                'link': shortened_url,
                'http_code': HTTP_Codes.OK.value}

            return self.send(response)
        except Exception as ex:
            return self.send(ex.__dict__)

from flask import request, jsonify
from src.api.services.shortener import Shortener_Service


class Shortener_Controller():

    def __init__(self):
        self._service = Shortener_Service()

    def shorten_url(self):
        payload = request.json
        provider = payload['provider'].lower()

        if provider == 'bitly':
            self._service.shorten_url_bitly(payload)
        elif provider == 'tinyurl':
            self._service.shorten_url_tinyurl(payload)
        else: 
            return jsonify({
                'status': False,
                'error': 'Invalid provider ' + payload['provider'] + ' given...'
            })

        return jsonify(payload)

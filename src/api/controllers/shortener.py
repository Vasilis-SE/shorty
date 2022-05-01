from flask import request, jsonify
from src.api.services.shortener import Shortener_Service


class Shortener_Controller():

    def __init__(self):
        self._service = Shortener_Service()

    def shorten_url(self):
        payload = request.json
        return jsonify(payload)

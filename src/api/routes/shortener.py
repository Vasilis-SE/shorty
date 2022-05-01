from flask import Blueprint

from src.api.controllers.shortener import Shortener_Controller

shortener_routes = Blueprint('shortlinks', __name__)

_controller = Shortener_Controller()


@shortener_routes.route('/shortlinks', methods=['POST'])
def shorten_url():
    return _controller.shorten_url()

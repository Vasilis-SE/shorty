from flask import Blueprint
from flasgger.utils import swag_from
from src.api.controllers.shortener import Shortener_Controller

shortener_routes = Blueprint('shortlinks', __name__)

_controller = Shortener_Controller()


@shortener_routes.route('/shortlinks', methods=['POST'])
@swag_from('../../../docs/shorten_url.yml')
def shorten_url():
    return _controller.shorten_url()

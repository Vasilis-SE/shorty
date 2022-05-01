from flask import Flask
from dotenv import dotenv_values

# Import all route files
from src.api.routes.shortener import shortener_routes
from src.api.routes.greetings import greetings

config = dotenv_values("./config/.env")


class Server():

    def __init__(self, **settings):
        self.settings = settings
        self.init_server()

    # Initialize flask server
    def init_server(self):
        self.app = Flask(__name__)
        self.configure_settings()
        self.configure_routes()

    # Set settings for the server
    def configure_settings(self):
        self.app.config.update({
            'DEBUG': True,
            'TESTING': False,
        })

        # Replace default settings if there are any given
        if self.settings:
            self.app.config.update(self.settings)

    # Set all routes for the server
    def configure_routes(self):
        self.app.register_blueprint(greetings, url_prefix='/api/v1')
        self.app.register_blueprint(shortener_routes, url_prefix='/api/v1')

    # Run server
    def run(self):
        self.app.run(host='0.0.0.0', port=config['API_PORT'], debug=True)

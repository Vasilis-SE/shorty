import os
from flask import Flask
from dotenv import load_dotenv
from flasgger import Swagger

# Import all route files
from src.api.routes.shortener import shortener_routes

load_dotenv("./config/.env")


class Server():
    """ Main class that initializes the server that will run and also Flask to
        handle requests. It starts creates a new Flask instance then sets up its
        settings, then sets up all the routes that the API will listen to, then sets up
        the OpenAPI documentation and finally runs the server.

        Properties: 
            app         The application instance.
            settings    External setting that can be passed upon initialization to replace the default ones.
    """

    def __init__(self, **settings):
        self.settings = settings
        self.init_server()

    # Initialize flask server
    def init_server(self):
        self.app = Flask(__name__)
        self.configure_settings()
        self.configure_routes()
        self.configure_openapi()

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
        self.app.register_blueprint(shortener_routes, url_prefix='/api/v1')

    # Configures open api to run on <domain>:3000/apidocs
    def configure_openapi(self):
        swag = Swagger(self.app)

    # Run server
    def run(self):
        self.app.run(host='0.0.0.0', port=os.getenv('API_PORT'), debug=True)

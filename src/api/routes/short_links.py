from flask import Blueprint

short_links_routes = Blueprint('shortlinks', __name__)

@short_links_routes.route('/', methods=['POST'])
def create_shortlink():
    print('Iam gonna short your link now...')

from flask import Blueprint

greetings = Blueprint('greetings', __name__)

@greetings.route('/', methods=['GET'])
def hello_world():
    print('Iam gonna short your link now...')

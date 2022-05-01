from flask import Blueprint

greetings = Blueprint('greetings', __name__)

@greetings.route('/greetings', methods=['GET'])
def hello_world():
    return 'Hello there!'

from flask import Flask
from dotenv import dotenv_values

config = dotenv_values("./config/.env")
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config['API_PORT'], debug=True)

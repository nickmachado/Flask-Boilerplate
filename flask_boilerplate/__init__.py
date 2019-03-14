from flask import Flask

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return 'I wanna go home and nap right now.'

    return app

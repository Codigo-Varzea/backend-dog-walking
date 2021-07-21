from flask import Flask
from src.api import api as api_blueprint

def create_app():
    app = Flask(__name__)

    register_api(app)

    return app

def register_api(app):
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

app = create_app()

from flask import Flask
from src.api.passeios import passeios

def create_app():
    app = Flask(__name__)

    register_api(app)

    return app

def register_api(app):
    app.register_blueprint(passeios)

app = create_app()

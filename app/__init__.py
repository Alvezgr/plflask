"""module for create app"""
from flask import Flask
from flask_bootstrap import Bootstrap
from app.config import Config
from auth import auth

def create_app():
    """create app method"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    app.register_blueprint(auth)
    return app

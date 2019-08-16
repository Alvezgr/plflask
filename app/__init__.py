"""module for create app"""
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config
from auth import auth


login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    """create app method"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    login_manager.init_app(app)
    app.register_blueprint(auth)
    return app

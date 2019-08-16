"""module for create app"""
from flask import Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from app.config import Config
from auth import auth
from .models import UserModel

LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.login_view = 'auth.login'


@LOGIN_MANAGER.user_loader
def load_user(username):
    """return the queery"""
    return UserModel.query(username)


def create_app():
    """create app method"""
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)
    LOGIN_MANAGER.init_app(app)
    app.register_blueprint(auth)
    return app

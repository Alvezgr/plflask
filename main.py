"""Flask App trainign course"""

import unittest
from flask import (
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
    flash
    )
from flask_bootstrap import Bootstrap
from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users
APP = create_app()

TODO = ['Get some coffe', 'wash dishes', 'buy a dog']


@APP.cli.command()
def test():
    """method for running test"""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@APP.errorhandler(404)
def not_found(error):
    """Error handler for not found"""
    return render_template('404.html', error=error)

@APP.errorhandler(500)
def server_error(error):
    """Error handler for internal server error"""
    return render_template('500.html', error=error)

@APP.route('/')
def index():
    """the index view"""
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response

@APP.route('/hello')
def hello():
    """In hello we display the ip"""
    user_ip = session.get('user_ip')
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': TODO,
        'username': username
        }
    users = get_users()
    for user in users:
        print(user.id)
    return render_template('hello.html', **context)

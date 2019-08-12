"""Flask App trainign course"""

import unittest
from flask import (
    Flask,
    request,
    make_response,
    redirect,
    render_template,
    session,
    url_for,
    flash
    )
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

APP = Flask(__name__)
bootstrap = Bootstrap(APP)

APP.config['SECRET_KEY'] = 'SUPER SECRETO'

TODO = ['Get some coffe', 'wash dishes', 'buy a dog']


class LoginForm(FlaskForm):
    """Class for login form"""
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

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

@APP.route('/hello', methods=['GET', 'POST'])
def hello():
    """In hello we display the ip"""
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': user_ip,
        'todos': TODO,
        'login_form': login_form,
        'username': username
        }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('username was registered!')
        return redirect(url_for('index'))
    return render_template('hello.html', **context)

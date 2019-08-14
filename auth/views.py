"""Views module"""
from flask import (
    redirect,
    render_template,
    session,
    url_for,
    flash
    )
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Login view"""

    login_form = LoginForm()

    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('username was registered!')
        return redirect(url_for('index'))
    return render_template('login.html', **context)

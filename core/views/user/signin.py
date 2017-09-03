# -*- coding: utf-8 -*-

import urllib
from . import client
from flask import request
from flask import render_template
from flask import redirect, url_for
from flask_login import UserMixin
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from core.extension import login_manager
from core.models import User
from core.views.common import render_json


class ClientLoginUser(User, UserMixin):

    def __init__(self, user):
        self.user = user

    def get_id(self):
        return unicode(self.user.id)

@login_manager.user_loader
def load_user(userid):
    user = User.get_by_id(int(userid))
    return ClientLoginUser(user)


@client.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        user = User.query.filter_by(
            active=True,
            name=request.form['name'],
            password=request.form['password']
        ).first()
        if not user:
            return render_json(1, {'err_no': 'pwd_error', 'input': 'password'})

        login_user(ClientLoginUser(user))
        next = request.form.get('next', '')
        if next:
            next = urllib.unquote(next)
            return render_json(0, {'href': next, 'delaySuccess': True})
        return render_json(0, {'href': '/client/dashboard', 'delaySuccess': True})
    return render_template('/user/signin.html')


@client.route('/signout', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for('client.signin'))


@client.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('/user/dashboard.html')

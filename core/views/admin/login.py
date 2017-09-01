# -*- coding: utf-8 -*-

import urllib
from . import admin
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import UserMixin
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from core.extension import login_manager
from core.views.common import render_json
from core.models import AdminUser


class LoginUser(UserMixin):
    def __init__(self, user):
        self.user = user

    def get_id(self):
        return unicode(self.user.id)


@login_manager.user_loader
def load_user(userid):
    user = AdminUser.get_by_id(int(userid))
    return LoginUser(user)


@admin.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        user = AdminUser.query.filter_by(
            active=True,
            username=request.form['username'],
            password=request.form['pwd']
        ).first()
        if not user:
            return render_json(1, {'err_no': 'pwd_error', 'input': 'pwd'})

        login_user(LoginUser(user))
        next = request.form.get('next', '')
        if next:
            next = urllib.unquote(next)
            return render_json(0, {'href': next, 'delaySuccess': True})
        return render_json(0, {'href': '/admin/dashboard', 'delaySuccess': True})
    return render_template('/admin/signin.html')


@admin.route('/signout', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for('admin.signin'))


@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('/admin/dashboard.html')

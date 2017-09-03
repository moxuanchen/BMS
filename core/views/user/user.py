# -*- coding: utf-8 -*-

from . import client
from flask_login import login_required
from flask import request, redirect, url_for
from flask import render_template
from flask import current_app
from flask_login import current_user
from core.views.common import render_json


@client.route('/password/change', methods=['GET', 'POST'])
@login_required
def chanage_password():
    if request.method == 'POST':
        info = {
            'old': request.form['old'],
            'new': request.form['new'],
            'double': request.form['double']
        }

        if info['old'] != current_user.user.password:
            return render_json(1, {'err_no': 'pwd_error', 'input': 'old'})
        if info['new'] != info['double']:
            return render_json(1, {'err_no': 'pwd_error', 'input': 'double'})
        current_user.user.update(password=info['new'])
        return render_json(0, {'href': '/client/dashboard', 'delaySuccess': True})
    return render_template('user/password.html')

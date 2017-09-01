# -*- coding: utf-8 -*-

from . import admin
from flask import request
from core.models import User
from flask import url_for
from flask import redirect
from flask_login import login_required
from flask import render_template
from sqlalchemy import or_
from core.views.common import render_json


@admin.route('/users', methods=['GET'])
@login_required
def company_users():
    users = User.query.filter_by(active=True).all()
    return render_template("admin/user.html", users=users, count=len(users))


@admin.route('/user/add', methods=['GET', 'POST'])
@login_required
def user_add():
    if request.method == 'POST':
        user = {
            'name': request.form['name'],
            'gender': request.form['gender'],
            'number': request.form['number'],
            'phone': request.form['phone'],
            'department': request.form['department'],
        }

        User.create(**user)
        return render_json(0, {'href': '/admin/users', 'delaySuccess': True})
    return render_template('admin/user_add.html')


@admin.route('/user/edit', methods=['GET', 'POST'])
@login_required
def user_edit():
    user_id = request.args.get('id')
    user = User.get_by_id(user_id)
    print request.method
    if request.method == 'POST':
        print 'YES'
        user_info = {
            'name': request.form['name'],
            'gender': request.form['gender'],
            'number': request.form['number'],
            'phone': request.form['phone'],
            'department': request.form['department'],
        }

        print user
        user.update(**user_info)
        print 'xxxxxxx'
        return render_json(0, {'href': '/admin/users', 'delaySuccess': True})
    return render_template('admin/user_edit.html', user=user)


@admin.route('/user/delete', methods=['GET', 'POST'])
@login_required
def user_delete():
    user_id = request.args.get('id')
    user = User.get_by_id(user_id)
    user.update(active=False)
    return redirect(url_for('admin.company_users'))

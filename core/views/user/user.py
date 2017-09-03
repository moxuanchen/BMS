# -*- coding: utf-8 -*-

from . import client
from flask_login import login_required
from flask import request, redirect, url_for
from flask import render_template
from flask import current_app
from flask_login import current_user
from core.views.common import render_json


@client.route('/user/edit', methods=['GET', 'POST'])
@login_required
def school_students():
    pass
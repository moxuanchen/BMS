# -*- coding: utf-8 -*-

import json
from . import admin
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask_login import login_required
from core.views.common import render_json


@admin.route('/books', methods=['GET'])
@login_required
def books():
    pass


@admin.route('/book/add', methods=['GET', 'POST'])
@login_required
def video_add():
    pass


@admin.route('/book/edit', methods=['GET'])
@login_required
def video_play():
    pass


@admin.route('/book/delete', methods=['GET', 'POST'])
@login_required
def video_detail():
    pass

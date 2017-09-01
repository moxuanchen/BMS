# -*- coding: utf-8 -*-

from . import school
from flask import request
from flask import render_template
from flask_login import login_required
from flask_login import current_user


@school.route('/video', methods=['GET'])
@login_required
def video():
    pass


@school.route('/video/play', methods=['GET'])
@login_required
def video_play():
    pass

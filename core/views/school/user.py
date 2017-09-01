# -*- coding: utf-8 -*-

import json
import time
import hashlib
import requests
import datetime
from . import school
from sqlalchemy import or_
from core.utils import Vcode
from flask_login import login_required
from flask import request, redirect, url_for
from core.models import Student, School
from flask import render_template
from flask import current_app
from flask_login import current_user
from core.views.common import render_json
from core.views.common import render_students


@school.route('/students', methods=['GET', 'POST'])
@login_required
def school_students():
    pass

@school.route('/student/add', methods=['GET', 'POST'])
@login_required
def school_student_add():
    pass


@school.route('/student/edit', methods=['GET', 'POST'])
@login_required
def school_student_detail():
    pass


@school.route('/student/delete', methods=['POST'])
@login_required
def school_student_delete():
    pass


@school.route('/student/update', methods=['POST'])
@login_required
def school_student_update():
    pass

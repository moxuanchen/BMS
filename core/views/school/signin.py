# -*- coding: utf-8 -*-

import urllib
from flask import render_template
from flask import redirect, url_for
from flask_login import UserMixin
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from core.extension import login_manager
from core.views.common import render_json


class SchoolLoginUser(School, UserMixin):

    def __init__(self, school):
        self.school = school

    def get_id(self):
        return unicode(self.school.id)


@login_manager.user_loader
def load_user(userid):
    school = School.get_by_id(int(userid))
    return SchoolLoginUser(school)


@school.route('/signin', methods=['GET', 'POST'])
def school_signin():
    pass

@school.route('/dashboard', methods=['GET', 'POST'])
@login_required
def school_dashboard():
    pass


@school.route('/signout', methods=['GET'])
@login_required
def school_logout():
    pass

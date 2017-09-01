# -*- coding: utf-8 -*-

import sys
from flask import Flask
from flask import request
from core.settings import get_config_obj
from core.views.admin import admin
from core.extension import login_manager
from core.extension import db
from flask import redirect, url_for


def create_app(config=get_config_obj()):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(admin)
    login_manager.init_app(app)
    db.init_app(app)
    return app


@login_manager.unauthorized_handler
def unauthorized():
    if request.blueprint == 'admin':
        return redirect(url_for('admin.signin', next=request.url))
    else:
        return redirect(url_for('school.school_signin', next=request.url))

# -*- coding: utf-8 -*-

from flask import Blueprint

admin = Blueprint('admin', __name__, static_folder='static', template_folder='templates', url_prefix='/admin')

import login
import book
import user

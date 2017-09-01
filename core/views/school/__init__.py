# -*- coding: utf-8 -*-

from flask import Blueprint

school = Blueprint('school', __name__, template_folder='templates', static_folder='static', url_prefix='/school')

import signin
import student

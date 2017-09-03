# -*- coding: utf-8 -*-

from flask import Blueprint

client = Blueprint('client', __name__, template_folder='templates', static_folder='static', url_prefix='/client')

import signin
import user
import book

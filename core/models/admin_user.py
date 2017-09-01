# -*- coding: utf-8 -*-

import datetime
from core.database import db
from core.database import Model
from core.database import SurrogatePK


class AdminUser(Model, SurrogatePK):

    __tablename__ = 'admin_user'

    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    create_at = db.Column(db.DateTime, default=datetime.datetime.now())

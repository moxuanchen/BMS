# -*- coding: utf-8 -*-


import datetime
from core.database import db
from core.database import Model
from core.database import SurrogatePK


class User(Model, SurrogatePK):

    __tablename__ = "user"

    name = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    number = db.Column(db.String(16), nullable=False)
    phone = db.Column(db.String(16), nullable=True)
    department = db.Column(db.String(32), nullable=True)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

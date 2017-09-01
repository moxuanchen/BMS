import datetime
from core.database import db
from core.database import Model
from core.database import SurrogatePK


class Book(Model, SurrogatePK):

    __tablename__ = "book"

    name = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(32), nullable=False)
    price = db.Column(db.String(8), nullable=False)
    isbn = db.Column(db.String(16), nullable=True)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

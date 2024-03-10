from flask_login import UserMixin

from .database import db


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300))  # password: hachage + salt + cryptage

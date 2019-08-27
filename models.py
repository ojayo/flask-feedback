""" Models for the Flask Feedback App """

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


class User(db.Model):
    """ Create a User model """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.Text(20), nullable=False, unique=True)
    email = db.Column(db.Text(50), nullable=False)
    first_name = db.Column(db.Text(30), nullable=False)
    last_name = db.Column(db.Text(30), nullable=False)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
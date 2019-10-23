# native modules
import datetime
import os

# author modules
from app import db, bcrypt


class Role(db.Model):
    """ Role Model for storing many types of role """
    __table__name = 'roles'

    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(25), index=True, nullable=False)

    users = db.relationship('User', backref=db.backref('role', lazy='joined'), lazy=True)


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), index=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'), nullable=False, default=1)

    webpages = db.relationship('WebPage', backref=db.backref('user', lazy='joined'), lazy=True)

    def __init__(self, password):
        self.password_hash = bcrypt.generate_password_hash(password, os.getenv('BCRYPT_LOG_ROUNDS')).decode('utf-8')
        self.registered_on = datetime.datetime.now()


class WebPage(db.Model):
    """  WebPage Model for storing webpages registry by user """
    webpage_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    webpage_url = db.Column(db.String(40), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    images = db.relationship('Images', backref=db.backref('webpage', lazy='joined'), lazy=True)
    # articles = db.relationship('Articles', lazy=True)


class Images(db.Model):
    """ Image Model for storing images that comes from Webpages """
    name = db.Column(db.String(30), nullable=False)
    image_url = db.Column(db.String(50), nullable=False)
    extension = db.Column(db.String(5), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    webpage_id = db.Column(db.Integer, db.ForeignKey('webpage.webpage_id'), nullable=False)


class Articles(db.Model):
    """ Articles model for storing articles that comes from Webpages """
    pass

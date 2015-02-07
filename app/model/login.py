# -*- coding: utf-8 -*-


from datetime import datetime
from flask.ext.security import SQLAlchemyUserDatastore, UserMixin, RoleMixin
from app.model import db

# Define models required for Flask-Security
roles_users = db.Table('roles_users', db.Column('user_id', db.Integer(), 
    db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(),
    db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)


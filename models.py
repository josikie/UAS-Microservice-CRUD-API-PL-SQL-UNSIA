import os
from flask import Flask, render_template_string
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import (
    Column,
    String,
    Integer,
    create_engine,
    ForeignKey,
    Boolean,
    DateTime,
    LargeBinary
)

import json

from dotenv import load_dotenv
from encryption import (
    decrypt,
    encrypt,
    BLOCK_SIZE,
    pad,
    unpad,
    SALT
)

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")

database_name = 'microservice'
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    with db.app.app_context():
        db.init_app(app)
        db.create_all()


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(LargeBinary, nullable=False, unique=True)
    password = Column(LargeBinary, nullable=False, server_default='')
    authenticated = Column(Boolean, default=False)

    def __init__(self, email, password):
        self.email =  email
        self.password = password

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'email': self.email
        }
    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return str(self.id)

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(50), unique=True)

#     def __init__(self, name):
#         self.name =  name

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()
    
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
    
#     def format(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }

# class UserRoles(db.Model):
#     __tablename__ = 'user_roles'
#     id = Column(Integer(), primary_key=True)
#     user_id = Column(Integer(), ForeignKey('users.id', ondelete='CASCADE'))
#     role_id = Column(Integer(), ForeignKey('roles.id', ondelete='CASCADE'))

#     def __init__(self, user_id, role_id):
#         self.user_id = user_id
#         self.role_id = role_id

#     def insert(self):
#         db.session.add(self)
#         db.session.commit()

#     def update(self):
#         db.session.commit()
    
#     def delete(self):
#         db.session.delete(self)
#         db.session.commit()
    
#     def format(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'role_id': self.role_id 
#         }
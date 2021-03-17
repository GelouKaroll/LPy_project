from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    id     = db.Column(db.Integer, primary_key=True)
    login  = db.Column(db.String(80), nullable=False, unique=True)
    #email = db.Column(db.String(120), nullable=False, unique=True)
    date   = db.Column(db.DateTime(), default=datetime.utcnow)
   
class Point(db.Model):
    __tablename__ = 'Points'
    id      = db.Column(db.Integer, primary_key=True)
    #login  = db.Column(db.String, nullable=False)
    user_id = db.Column(db.String(), db.ForeignKey(User.id), index=True, nullable=False)
    date    = db.Column(db.DateTime(), default=datetime.utcnow)
    x       = db.Column(db.String, nullable=False)
    y       = db.Column(db.String, nullable=False)
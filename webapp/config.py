import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bla-bla-bla'
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'project_db.db')
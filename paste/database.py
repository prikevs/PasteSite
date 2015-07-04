#coding:utf8

from flask.ext.sqlalchemy import SQLAlchemy
from . import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relative/../../test.db'
db = SQLAlchemy(app)

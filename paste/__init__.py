#coding:utf8

from flask import Flask
app = Flask(__name__)
from . import views

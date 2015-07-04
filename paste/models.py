#coding:utf8

from .database import db
from datetime import datetime


class Paste(db.Model):
    __tablename__ = "pastes"

    id = db.Column(db.Integer, primary_key=True)
    poster = db.Column(db.String(30))
    syntax = db.Column(db.String(10))
    post_time = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.Text) 

    def __init__(self, poster, syntax, content, post_time=None):
        self.poster = poster
        self.syntax = syntax
        self.content = content
        if post_time:
            self.post_time = post_time

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return '<Poster %r>' % self.poster



def create_paste(poster, syntax, content, post_time=None):
    paste = Paste(poster, syntax, content, post_time)
    paste.save()
    return paste

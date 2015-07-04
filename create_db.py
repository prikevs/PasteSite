#!/usr/bin/env python2

from paste.database import db

if __name__ == '__main__':
    db.create_all()

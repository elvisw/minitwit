# -*- coding: utf-8 -*-
"""
    MiniTwit
    ~~~~~~~~

    A microblogging application written with Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from flask import Flask, session, g

# create our little application :)
app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)

from app import views, db, filters

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = db.query_db('select * from user where user_id = ?',
                          [session['user_id']], one=True)


if __name__ == '__main__':
    db.init_db()
    app.run()

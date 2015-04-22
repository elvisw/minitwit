# -*- coding: utf-8 -*-
"""
    MiniTwit
    ~~~~~~~~

    A microblogging application written with Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from hashlib import md5
from datetime import datetime
from flask import Flask, session, g

# create our little application :)
app = Flask(__name__)
app.config.from_object('config')
app.config.from_envvar('MINITWIT_SETTINGS', silent=True)

def format_datetime(timestamp):
    """Format a timestamp for display."""
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')


def gravatar_url(email, size=80):
    """Return the gravatar image for the given email address."""
    return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
        (md5(email.strip().lower().encode('utf-8')).hexdigest(), size)

# add some filters to jinja
app.jinja_env.filters['datetimeformat'] = format_datetime
app.jinja_env.filters['gravatar'] = gravatar_url

from app import views, db

if __name__ == '__main__':
    db.init_db()
    app.run()

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = db.query_db('select * from user where user_id = ?',
                          [session['user_id']], one=True)
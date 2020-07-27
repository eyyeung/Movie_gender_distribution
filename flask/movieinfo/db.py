import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

# g is a special object that is unique for each request
# used to store data that might be accessed by multiple function during the request
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            # current_app is another object that points to the Flask application handling the requests
            # we could set the DATABASE in the config file
            current_app.config['DATABASE'],
            detect_types= sqlite3.PARSE_DECLTYPES
        )
        # return rows that behave like dicts - allow for accessing columns by name
        g.db.row_factory = sqlite3.Row

    return g.db

# if g.db was set, then close it
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# close_db and init_db_command need to be registered with the app instance, but we are using a factory function, so that instance isn't available. Need to define them with a function instead
def init_app(app):
    # teardown_appcontext tells Flask to call that function when cleaning up after returning the response
    app.teardown_appcontext(close_db)
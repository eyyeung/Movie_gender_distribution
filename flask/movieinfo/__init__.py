from flask import Flask
import os

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DATABASE'] = 'movieinfo/movieinfo.sqlite'

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import movies
    app.register_blueprint(movies.bp)
    app.add_url_rule('/',endpoint='index')

    return app


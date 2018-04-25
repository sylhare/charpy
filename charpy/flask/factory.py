# -*- coding: utf-8 -*-
"""
Use export FLASK_APP="charpy.factory:create_app()"


"""
from flask import Flask
from charpy import TEST_DATABASE_URI
from werkzeug.utils import find_modules, import_string


def create_app(config=None, debug=False):
    app = Flask(__name__)
    app.debug = debug

    app.config.update(dict(
        DATABASE=TEST_DATABASE_URI,
        DEBUG=True,
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """Automagically register all blueprint named bp in packages

    Check the argument 'bp' in all the modules in the folder inserted in findmodules
    then register all blueprints in the app
    """
    for name in find_modules('charpy.flask.blueprints', recursive=True):
        mod = import_string(name)

        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


if __name__ == "__main__":  # pragma: no cover
    app = create_app(debug=True)
    # print(app.blueprints)

    app.run()


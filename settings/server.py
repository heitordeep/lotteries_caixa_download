import os

from flask import Flask

PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]


def create_app(app_name=PKG_NAME, **kwargs):
    app = Flask(app_name)
    app.config['JSON_AS_ASCII'] = False

    from api.api import api
    from web.main import app_web

    app.register_blueprint(app_web)
    app.register_blueprint(api)

    return app

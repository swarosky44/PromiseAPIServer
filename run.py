# encoding=UTF-8
from flask import Flask
from config import default
from RESTfulApi.app import api_bp
# from RESTfulApi.models import register_database


def create_app(**config):
    app = Flask(__name__)
    register_config(app, config)
    # register_database(app)
    register_routes(app)
    return app


def register_config(app, config):
    if config.get("DEBUG") is True:
        app.debug = True

    app.config.from_object(default)


def register_routes(app):
    app.register_blueprint(api_bp, url_prefix="/api")


if __name__ == "__main__":
    print("Flask Server is already!")
    create_app(debug=True).run()

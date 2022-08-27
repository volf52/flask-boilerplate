# -*- coding: utf-8 -*-
import os

from flask import Flask, redirect, request

from app import blueprints
from app.jinja import register_jinja_mapping


def init_config(app: "Flask"):
    app.config.from_object("conf.default")
    # app.config.from_pyfile('config.py')
    # app.config.from_object(f"config.{os.environ.get('APP_CONFIG')}")


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    init_config(app)

    # Sentry init

    # Db Init

    # Cache init

    # Jinja mapping
    register_jinja_mapping(app)

    # debug toolbar ext

    # https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.url_map
    app.url_map.strict_slashes = app.config["FLASK_STRICT_SLASHES"]

    @app.before_request
    async def app_before_request():
        req_path = request.path

        if req_path != "/" and req_path.endswith("/"):
            return redirect(req_path[:-1], 301)

    # register error handlers

    blueprints.register_blueprints(app)

    # init cli app

    return app

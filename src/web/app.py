# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.web.controllers import register_routes

# def init_config(app: "Flask"):
#     app.config.from_object("src.infra.config.default")
#     # app.config.from_pyfile('config.py')
# app.config.from_object(f"config.{os.environ.get('APP_CONFIG')}")


def create_app():
    app = FastAPI(title="PythonDDD", debug=True)

    # init_config(app)

    # Sentry init

    # Db Init

    # Cache init

    # Jinja mapping
    # register_jinja_mapping(app)

    # debug toolbar ext

    # register error handlers

    register_routes(app)

    # init cli app

    return app

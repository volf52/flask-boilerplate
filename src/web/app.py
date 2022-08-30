# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.infra.logging.loguru_logger import init_logging
from src.web.controllers import register_routes


def create_app():  # noqa: ANN201
    init_logging()

    app = FastAPI(title="PythonDDD", debug=True, default_response_class=ORJSONResponse)

    # Sentry init

    # Db Init

    # Cache init

    # debug toolbar ext

    # register error handlers

    register_routes(app)

    # init cli app

    return app

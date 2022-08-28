# -*- coding: utf-8 -*-
from flask_restful import Api

from src.web.controllers.health import HealthController


def register_routes(api: "Api"):
    api.add_resource(HealthController, "/health")

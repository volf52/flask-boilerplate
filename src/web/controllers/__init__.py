# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.web.controllers.health_controller import HealthRouter


def register_routes(api: "FastAPI") -> None:
    api.include_router(HealthRouter().router)

# -*- coding: utf-8 -*-
from fastapi import FastAPI

from src.web.controllers.health import router as heath_router


def register_routes(api: "FastAPI") -> None:
    api.include_router(heath_router)

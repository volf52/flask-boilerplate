# -*- coding: utf-8 -*-
from typing import Any

from antidote import world
from classy_fastapi import Routable, get

from src.app import AppLogger
from src.infra.logging import get_logger


class HealthRouter(Routable):
    logger = world[AppLogger]

    def __init__(self, logger: Any = get_logger()) -> None:
        super().__init__()

        self.logger = logger

    @get("/health")
    async def health(self):
        self.logger.info("hello there")

        return {"status": "ok"}

# -*- coding: utf-8 -*-

from antidote import inject, wire
from classy_fastapi import Routable, get

from src.app import AppLogger


@wire
class HealthRouter(Routable):
    logger: AppLogger  # = world[AppLogger]

    def __init__(self, logger: AppLogger = inject.me()) -> None:
        super().__init__()

        self.logger = logger

    @get("/health")
    async def health(self):
        self.logger.info("hello there")

        return {"status": "ok"}

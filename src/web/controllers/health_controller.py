# -*- coding: utf-8 -*-
from logging import Logger
from typing import Any

from classy_fastapi import Routable, get

from src.infra.logging import get_logger

# logger = logging.getLogger("HealthController")


class HealthRouter(Routable):
    logger: Logger

    def __init__(self, logger: Any = get_logger()) -> None:
        super().__init__()

        self.logger = logger

    @get("/health")
    async def health(self):
        self.logger.info("hello there")

        return {"status": "ok"}

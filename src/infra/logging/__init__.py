# -*- coding: utf-8 -*-
from __future__ import annotations

from functools import lru_cache
from typing import TYPE_CHECKING, Any

from antidote import implements
from loguru import logger

from infra.logging.loguru_logger import init_logging
from src.app import AppLogger

if TYPE_CHECKING:
    from loguru import Logger


@lru_cache(maxsize=1)  # singleton
def get_logger() -> Logger:
    return logger


@implements.protocol[AppLogger]()
class LoggerService(AppLogger):
    def info(*args: Any) -> None:
        logger.info(*args)

    def debug(*args: Any) -> None:
        logger.debug(*args)


__all__ = ["init_logging", "get_logger", "LoggerService"]

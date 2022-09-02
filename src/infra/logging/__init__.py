# -*- coding: utf-8 -*-
from functools import lru_cache

from loguru import logger


@lru_cache(maxsize=1)  # singleton
def get_logger():  # ignore: type
    return logger

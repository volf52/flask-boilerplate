# -*- coding: utf-8 -*-
from typing import Any, Protocol, runtime_checkable

from antidote import interface


@interface
@runtime_checkable
class AppLogger(Protocol):
    def info(*args: Any) -> None:
        ...

    def debug(*args: Any) -> None:
        ...

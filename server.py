# -*- coding: utf-8 -*-
import asyncio
import signal
from typing import Any

import uvloop
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.infra.config import default as default_config
from src.web.app import create_app

hypercorn_config = Config()
hypercorn_config.bind = [f"0.0.0.0:{default_config.PORT}"]

application = create_app()

shutdown_event = asyncio.Event()


def _signal_handler(*_: Any) -> None:
    shutdown_event.set()


def get_event_loop() -> asyncio.AbstractEventLoop:
    uvloop.install()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    return loop


def setup_signal_handlers(loop: asyncio.AbstractEventLoop):
    loop.add_signal_handler(signal.SIGTERM, _signal_handler)


if __name__ == "__main__":
    loop = get_event_loop()

    setup_signal_handlers(loop)

    loop.run_until_complete(
        serve(application, hypercorn_config, shutdown_trigger=shutdown_event.wait)
    )

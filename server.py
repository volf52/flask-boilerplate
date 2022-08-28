# -*- coding: utf-8 -*-
import asyncio
import signal
from typing import Any

import uvloop
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.infra.config import default as default_config
from src.web.app import create_app

config = Config()

application = create_app()

shutdown_event = asyncio.Event()


def _signal_handler(*_: Any) -> None:
    shutdown_event.set()


if __name__ == "__main__":
    uvloop.install()

    config.bind = [f"0.0.0.0:{default_config.PORT}"]

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.add_signal_handler(signal.SIGTERM, _signal_handler)
    loop.run_until_complete(
        serve(application, config, shutdown_trigger=shutdown_event.wait)
    )

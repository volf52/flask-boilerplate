# -*- coding: utf-8 -*-
import asyncio

import uvloop
from hypercorn.asyncio import serve
from hypercorn.config import Config

from src.infra.config import default as default_config
from src.web.app import create_app

hypercorn_config = Config()
hypercorn_config.bind = [f"0.0.0.0:{default_config.PORT}"]

application = create_app()


def get_event_loop() -> asyncio.AbstractEventLoop:
    uvloop.install()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    return loop


if __name__ == "__main__":
    loop = get_event_loop()

    loop.run_until_complete(
        serve(
            application,
            hypercorn_config,
        )
    )

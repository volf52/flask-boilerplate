# -*- coding: utf-8 -*-
import pytest
from httpx import AsyncClient

from src.web.app import create_app

TEST_PORT = 9000


@pytest.fixture
def app():
    application = create_app()

    return application


@pytest.fixture
async def test_client(app):
    async with AsyncClient(app=app, base_url=f"http://127.0.0.1:{TEST_PORT}") as ac:
        yield ac

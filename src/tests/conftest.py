import asyncio
import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from config import BASE_URL
from core import create_app

application = create_app()


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.mark.asyncio
@pytest.fixture
async def test_app():
    async with LifespanManager(application):
        async with AsyncClient(app=application, base_url=BASE_URL) as client:
            yield client

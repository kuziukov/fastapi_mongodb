from core.mongodb import get_database


async def database():
    db = await get_database()
    yield db


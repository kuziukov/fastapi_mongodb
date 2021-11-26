from motor.motor_asyncio import AsyncIOMotorClient
from config import (
    DATABASE_URL,
    MONGO_DBNAME
)


class DataBase:
    client: AsyncIOMotorClient = None


db = DataBase()


async def get_client() -> AsyncIOMotorClient:
    return db.client


async def get_database() -> AsyncIOMotorClient:
    return db.client[MONGO_DBNAME]


async def connect_mongo():
    db.client = AsyncIOMotorClient(DATABASE_URL, authSource="admin")


async def close_mongo():
    db.client.close()

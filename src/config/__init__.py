from starlette.config import Config
from starlette.datastructures import Secret

config = Config(".env")

API_PREFIX = '/v1'
VERSION = '0.0.0'
BASE_URL = 'http://0.0.0.0:8000/v1/'

PROJECT_NAME: str = config("PROJECT_NAME", default="fastapi_mongodb")
DEBUG: bool = config("DEBUG", cast=bool, default=False)
SECRET_KEY: Secret = config("SECRET_KEY", cast=str)

MONGO_HOST: str = config("MONGO_HOST")
MONGO_DBNAME: str = config("MONGO_DBNAME")
MONGO_USER: str = config("MONGO_USER")
MONGO_PASSWORD: str = config("MONGO_PASSWORD")

DATABASE_URL: str = f'mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DBNAME}'

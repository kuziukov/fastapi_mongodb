from fastapi import FastAPI
from api.router_api import init_routes
from config import (
    PROJECT_NAME,
    DEBUG,
    VERSION
)
from core.cors import init_cors
from core.mongodb import (
    connect_mongo,
    close_mongo
)


def create_app() -> FastAPI:
    app = FastAPI(
        title=PROJECT_NAME,
        debug=DEBUG,
        version=VERSION,
        on_startup=[connect_mongo],
        on_shutdown=[close_mongo],
        middleware=[]
    )
    init_routes(app)
    init_cors(app)
    return app

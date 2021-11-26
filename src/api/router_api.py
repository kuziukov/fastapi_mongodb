from fastapi import (
    FastAPI,
    APIRouter
)
from api.resources.employees import employees_get_router

router_api = APIRouter(prefix='/v1')


def init_routes(app: FastAPI) -> None:
    router_api.include_router(employees_get_router)
    app.include_router(router_api)

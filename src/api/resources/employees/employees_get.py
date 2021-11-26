from typing import List
from fastapi import (
    APIRouter,
    Depends
)
from pydantic import BaseModel
from dependency import database
from schemas.employee import EmployeeSchemaRead

employees_get_router = APIRouter(
    tags=['employees']
)


class FiltersSchema(BaseModel):
    start: int = 0
    limit: int = 10


@employees_get_router.get(
    '/employees',
    summary='get employees method',
    description='method for getting employees',
    response_model=List[EmployeeSchemaRead]
)
async def employee_get(filters: FiltersSchema = Depends(), db_session=Depends(database)):
    employees = await db_session["employees"].find().skip(filters.start).limit(filters.limit).to_list(filters.limit)
    return employees

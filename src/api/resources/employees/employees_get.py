from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import (
    List,
    Optional
)
from fastapi import (
    APIRouter,
    Depends,
    Query
)
from dependency import database
from schemas.employee import EmployeeSchemaRead

employees_get_router = APIRouter(
    tags=['employees']
)


@dataclass
class FiltersSchema:
    start: int = 0
    limit: int = 10
    name: Optional[str] = None
    company: Optional[List[str]] = Query(None)
    job_title: Optional[List[str]] = Query(None)
    gender: Optional[str] = None
    start_age: Optional[int] = None
    end_age: Optional[int] = None
    start_salary: Optional[int] = None
    end_salary: Optional[int] = None
    start_join_date: Optional[datetime] = None
    end_join_date: Optional[datetime] = None


@employees_get_router.get(
    '/employees',
    summary='get employees method',
    description='method for getting employees',
    response_model=List[EmployeeSchemaRead]
)
async def employee_get(filters: FiltersSchema = Depends(), db_session=Depends(database)):
    query_kwargs = defaultdict(dict)

    if filters.name:
        query_kwargs['$text'].update({'$search': filters.name})

    if filters.company:
        query_kwargs['company'].update({'$in': filters.company})

    if filters.job_title:
        query_kwargs['job_title'].update({'$in': filters.job_title})

    if filters.gender:
        query_kwargs['gender'].update({'$eq': filters.gender})

    if filters.start_age:
        query_kwargs['age'].update({'$gte': filters.start_age})

    if filters.end_age:
        query_kwargs['age'].update({'$lte': filters.end_age})

    if filters.start_salary:
        query_kwargs['salary'].update({'$gte': filters.start_salary})

    if filters.end_salary:
        query_kwargs['salary'].update({'$lte': filters.end_salary})

    if filters.start_join_date:
        query_kwargs['join_date'].update({'$gte': filters.start_join_date})

    if filters.end_join_date:
        query_kwargs['join_date'].update({'$lte': filters.end_join_date})

    employees = await db_session["employees"]\
        .find(query_kwargs)\
        .skip(filters.start)\
        .limit(filters.limit)\
        .to_list(filters.limit)
    return employees

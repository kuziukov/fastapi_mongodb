from datetime import datetime
from bson import ObjectId
from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

from schemas.object_id import PyObjectId


class EmployeeSchema(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: str
    salary: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class EmployeeSchemaRead(EmployeeSchema):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

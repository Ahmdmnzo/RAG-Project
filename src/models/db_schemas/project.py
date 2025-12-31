from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class project(BaseModel):
    _id: Optional[ObjectId]
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validator_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')

        return value

    class Config:
        arbirtrary_types_allowed = True

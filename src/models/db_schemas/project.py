from pydantic import BaseModel, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    # غيرنا _id لـ id واستخدمنا Alias عشان يفهم إن أصلها في مونجو _id
    id: Optional[ObjectId] = Field(None, alias="_id")
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validator_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return value

    class Config:
        arbitrary_types_allowed = True
        # السطر ده ضروري عشان تقدر تنادي على id وتكتبها _id برضه لو حبيت
        populate_by_name = True

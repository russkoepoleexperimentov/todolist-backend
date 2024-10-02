from typing import Optional

from pydantic import BaseModel


class TaskCreateSchema(BaseModel):
    description: str


class BaseTaskSchema(TaskCreateSchema):
    done: bool


class TaskUpdateSchema(BaseModel):
    id: int
    description: Optional[str] = None
    done: Optional[bool] = None


class TaskOutSchema(BaseTaskSchema):
    id: int

    class Config:
        orm_mode = True

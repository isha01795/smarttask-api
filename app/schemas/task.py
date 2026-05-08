from pydantic import BaseModel, ConfigDict
from typing import Optional


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    user_id: int

    model_config = ConfigDict(from_attributes=True)
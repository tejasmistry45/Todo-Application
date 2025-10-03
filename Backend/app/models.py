from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Priority = Field(default=Priority.MEDIUM)
    tags: Optional[List[str]] = Field(default=[])


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    priority: Optional[Priority] = None
    completed: Optional[bool] = None
    tags: Optional[List[str]] = None


class TodoResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    priority: Priority
    completed: bool
    tags: List[str]
    created_at: datetime
    updated_at: datetime

from .enums import Status
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class TodoSerializer(BaseModel):
    id: str
    title: str

    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str
    description: str
    status: Status
    due_date: datetime
    responsible: str

    
class TodoUpdateSerializer(TodoCreateSerializer):
    pass

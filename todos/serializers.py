from .enums import Status
from pydantic import BaseModel
from datetime import datetime


class TodoCreateSerializer(BaseModel):
    title: str
    description: str
    status: Status
    due_date: datetime
    responsible: str

class TodoSerializer(TodoCreateSerializer):
    id: str

    class Config:
        orm_mode = True




class TodoUpdateSerializer(TodoCreateSerializer):
    pass

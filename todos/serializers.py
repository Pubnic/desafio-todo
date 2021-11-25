from .enums import Status
from pydantic import BaseModel
from datetime import datetime



class TodoSerializer(BaseModel):
    id: str


    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str
    status: str
    due_date: datetime
    responsible: str

class TodoUpdateSerializer(TodoCreateSerializer):
    
    pass

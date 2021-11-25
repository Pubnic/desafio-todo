from .enums import Status
from pydantic import BaseModel
from datetime import date, datetime



class TodoSerializer(BaseModel):
    id: str
    title: str


    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str 
    description: str
    status: str
    responsible:str   
    due_date: datetime
class TodoUpdateSerializer(TodoCreateSerializer):
    
    pass

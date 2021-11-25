from .enums import Status
from pydantic import BaseModel
from datetime import datetime



class TodoSerializer(BaseModel):
    id: str


    class Config:
        orm_mode = True


class TodoCreateSerializer(BaseModel):
    title: str
<<<<<<< HEAD
    status: str
    due_date: datetime
    responsible: str
=======
    description: str
    status: str
    due_date: str
    responsible:str   
>>>>>>> 78c32d0315a28d809258fd68dd73e7b421a4bdfe

class TodoUpdateSerializer(TodoCreateSerializer):
    
    pass

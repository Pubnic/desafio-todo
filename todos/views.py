from common.serializers import ErrorSerializer
from typing import List, Optional
from todos.db.services import TodosDBService
from fastapi import APIRouter, Query, status
from .serializers import TodoCreateSerializer, TodoSerializer, TodoAtributeSerializer, TodoUpdateSerializer

todo_router = APIRouter()
info_database = TodosDBService()
'''
GET todos/
'''
@todo_router.get('/')
def get_todo(title: Optional[List[str]] = Query(None), id: Optional[List[str]] = Query(None)):
    return info_database.get_todo()
    
''''
GET todos/{id}/

'''
@todo_router.get('/id/{id}', response_model=List[TodoSerializer])
def get_user(id: str):
    user_id = info_database.get_user(id)
    return user_id

'''
POST todos
'''
@todo_router.post('/', status_code=status.HTTP_201_CREATED,
    response_model=TodoSerializer
)
def create_todo(todo: TodoAtributeSerializer):
    new_todo = info_database.add_todo(todo.dict())
    return new_todo

'''
PUT todos
'''

''''
DELETE todos/{id}/
'''

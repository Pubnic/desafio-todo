from common.serializers import ErrorSerializer
from typing import List, Optional
from todos.db.services import TodosDBService
from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
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
@todo_router.get('/id/{todo_id}', response_model=List[TodoSerializer])
def get_user(todo_id: str):
    user_id = info_database.get_user(todo_id)
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
@todo_router.put('/id/{todo_id}')
def update_todo(todo_id: str, todo: TodoAtributeSerializer):
    up_todo = info_database.update_todo(todo_id)
    return up_todo
''''
DELETE todos/{id}/
'''
@todo_router.delete('/id/{todo_id}/')
def delete_user(todo_id: str, status_code=status.HTTP_204_NO_CONTENT):
    deleted = info_database.delete_user(todo_id)
    if not deleted:
        return JSONResponse(
            content={'message': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND
        )
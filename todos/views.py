from common.serializers import ErrorSerializer
from typing import List, Optional
from todos.db.services import TodosDBService
from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer
from .enums import Status


todo_router = APIRouter()
info_database = TodosDBService()


'''
GET todos/
'''

@todo_router.get('/')
async def get_todos():
    todos = info_database.get_todos()
    return todos

''''
GET todos/{id}/
'''

@todo_router.get('/id/{id}')
def get_todo(id: str):
    try:
        todo_id = info_database.get_todo(id)
        return todo_id
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)

'''
POST todos
'''
@todo_router.post('/', status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreateSerializer):
    new_todo = info_database.create_todo(todo)
    return new_todo

'''
PUT todos
'''

@todo_router.put('/id/{todo_id}')
def update_todo(todo_id: str, todo: TodoCreateSerializer):
    up_todo = info_database.update_todo(todo_id, todo)
    return up_todo

''''
DELETE todos/{id}/
'''

@todo_router.delete('/id/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):
    deleted = info_database.delete_todo(todo_id)
    if not deleted:
        return JSONResponse(
            content={'message': 'User not found'},
            status_code=status.HTTP_404_NOT_FOUND
        )
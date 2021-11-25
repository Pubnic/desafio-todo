from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from .db.models import TodoModel
from fastapi import APIRouter, status
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer, TodoGetSerializer
from typing import List 

todo_router = APIRouter()
banco_dados = TodosDBService()
'''
GET todos/
'''
@todo_router.get("/todos/", response_model=List(TodoSerializer))
def get_todos():
    todos = banco_dados.get_todos()


''''
GET todos/{id}/
'''
@todo_router.get("/todos/{id}")
def get_todos_id():
    todo = banco_dados.get_todo()
    if todo is None:
        return {"Error": "Todo not found"}
'''
POST todos
'''
@todo_router.post(
    "/todos/", 
    status_code=status.HTTP_201_CREATED, 
    response_model=TodoSerializer)
def create_todo(todo: TodoCreateSerializer):
    new_todo = banco_dados.create_todo(todo.dict())
    return new_todo
'''
PUT todos
'''
@todo_router.put("/todos/{id}",status_code=status.HTTP_201_CREATED)
def update_todo(todo: TodoUpdateSerializer):
    new_todo = banco_dados.create_todo
''''
DELETE todos/{id}/
'''
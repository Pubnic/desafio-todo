from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from fastapi import APIRouter, status
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer
from typing import List 

todo_router = APIRouter()
banco_dados = TodosDBService()

'''
GET todos/
'''
@todo_router.get("/")
def get_todos():
    todos = banco_dados.get_todos()
    return todos

''''
GET todos/{id}/
'''
@todo_router.get("/{todo_id}")
def get_todos_id(todo_id:str):
    todo = banco_dados.get_todo(todo_id)
    if todo is None:
        return ErrorSerializer

    return{"message": f"{todo}"}
'''
POST todos
'''
@todo_router.post(
    "/", 
    status_code=status.HTTP_201_CREATED,
    response_model=TodoCreateSerializer)
def create_todo(todo: TodoCreateSerializer):
    new_todo = banco_dados.create_todo(todo)
    return todo

'''
PUT todos
'''
@todo_router.put("/{todo_id}/",status_code=status.HTTP_201_CREATED)
def update_todo(todo_id: str, todo: TodoCreateSerializer):
    new_todo = banco_dados.update_todo(todo_id, todo)
    return todo

''''
DELETE todos/{id}/
'''
@todo_router.delete("/{todo_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id:str):
    new_todo = banco_dados.delete_todo(todo_id)
    if new_todo is None:
        return {"Error": "Todo not found"}
    return {"Message": "Todo deleted"}
    print("feito")
    
    
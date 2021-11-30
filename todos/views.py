from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from fastapi import APIRouter
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer


todo_router = APIRouter()
database = TodosDBService()

'''
GET todos/
'''


@todo_router.get('/')
def get_todos():
    alltodos = database.get_todos()
    return alltodos


''''
GET todos/{id}/
'''


@todo_router.get('/{id}/')
def get_todo(id: str):
    todo = database.get_todo()
    return todo

'''
POST todos
'''


@todo_router.post('/', status_code=201)
def create_todo(todo: TodoCreateSerializer):
    new_todo = database.create_todo(todo)
    return new_todo


'''
PUT todos
'''


@todo_router.put('/{id}')
def update_todo(id: str, todo: TodoUpdateSerializer):
    update = database.update_todo(id, todo)
    return update

''''
DELETE todos/{id}/
'''

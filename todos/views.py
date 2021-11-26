from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from fastapi import APIRouter, status, HTTPException
from .serializers import TodoCreateSerializer, TodoUpdateSerializer

todo_router = APIRouter()
service = TodosDBService ()
'''
GET todos/
'''
@todo_router.get ("/")
async def read_todos():
    return service.get_todos()
''''
GET todos/{id}/
'''
@todo_router.get ("/{id}")
async def read_todo(id):
    try:
        todo = service.get_todo(id)

        return todo
    except Exception as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND)
'''
POST todos
'''
@todo_router.post ("/", status_code=201)
async def create_todo(todo:TodoCreateSerializer):
    return service.create_todo(todo)
'''
PUT todos
'''
@todo_router.put ("/{id}")
async def read_todo(id):
    return service.put_todo(id)
''''
DELETE todos/{id}/
'''
@todo_router.delete ("/{id}", status_code=204)
async def read_todo(id):
    return service.delete_todo(id)

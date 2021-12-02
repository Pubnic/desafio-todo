from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService, TodoModel
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .serializers import (
    TodoCreateSerializer,
    TodoSerializer,
    TodoUpdateSerializer
)

todo_router = APIRouter()
service = TodosDBService()
'''
GET todos/
'''


@todo_router.get("/")
async def read_todos():
    return service.get_todos()
''''
GET todos/{id}/
'''


@todo_router.get(
    "/{id}",
    responses={
        404: {'model': ErrorSerializer},
    },
    response_model=TodoSerializer
)
async def read_todo(id):
    try:
        todo = service.get_todo(id)

        return todo
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404,
                            content=dict(error='Todo not found.'))
'''
POST todos
'''


@todo_router.post("/", status_code=201)
async def create_todo(todo: TodoCreateSerializer):
    return service.create_todo(todo)
'''
PUT todos
'''


@todo_router.put("/{id}")
async def put_todo(id, todo: TodoUpdateSerializer):
    try:
        return service.update_todo(id, todo)
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404,
                            content=dict(error='Todo not found.'))
''''
DELETE todos/{id}/
'''


@todo_router.delete("/{id}", status_code=204)
async def delete_todo(id):
    try:
        return service.delete_todo(id)
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404,
                            content=dict(error='Todo not found.'))

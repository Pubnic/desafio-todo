from todos.db.services import TodosDBService
from todos.db.models import TodoModel
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from .serializers import TodoCreateSerializer, TodoUpdateSerializer


todo_router = APIRouter()
info_database = TodosDBService()


'''
GET todos/
'''


@todo_router.get('/')
def get_todos():
    todos = info_database.get_todos()
    return todos


''''
GET todos/{id}/
'''


@todo_router.get('/id/{id}')
def get_todo(id: str):
    try:
        todo_id = info_database.get_todo(id)
    except TodoModel.DoesNotExist:
        return JSONResponse(
            status_code=404,
            content=dict(error='Todo not found')
        )
    return todo_id


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
def update_todo(todo_id: str, todo: TodoUpdateSerializer):
    up_todo = info_database.update_todo(todo_id, todo)
    return up_todo


'''
DELETE todos/{id}/
'''


@todo_router.delete('/id/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):
    deleted = info_database.delete_todo(todo_id)
    if not deleted:
        return {"Error": "Todo not found"}
    return {"Message": "Todo deleted"}

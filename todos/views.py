from common.serializers import ErrorSerializer
from starlette.responses import JSONResponse
from todos.db.services import TodosDBService
from fastapi import APIRouter, status, HTTPException
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer


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


@todo_router.get("/{todo_id}/", response_model=TodoSerializer)
def get_todos_id(todo_id: str):

    try:
        todo = banco_dados.get_todo(todo_id)

        return todo
    except Exception:
        return JSONResponse


'''
POST todos
'''


@todo_router.post("/", status_code=status.HTTP_201_CREATED)
def create_todo(todo: TodoCreateSerializer):
    return banco_dados.create_todo(todo)


'''
PUT todos
'''


@todo_router.put("/{todo_id}/")
def update_todo(todo_id: str, todo: TodoUpdateSerializer):

    return banco_dados.update_todo(todo_id, todo)


''''
DELETE todos/{id}/
'''


@todo_router.delete("/{todo_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):
    deleted = banco_dados.delete_todo(todo_id)
    if not deleted:
        return {"Error": "Todo not found"}
    return {"Message": "Todo deleted"}

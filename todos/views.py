from starlette.responses import JSONResponse
from todos.db.models import TodoModel
from todos.db.services import TodosDBService
from fastapi import APIRouter, status
from .serializers import TodoCreateSerializer, TodoUpdateSerializer
from .serializers import TodoSerializer

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
    except TodoModel.DoesNotExist:
        return JSONResponse(
            status_code=404,
            content=dict(error='Todo not found.')
        )


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

    try:
        return banco_dados.update_todo(todo_id, todo)

    except TodoModel.DoesNotExist:
        return JSONResponse(
            status_code=404,
            content=dict(error='Todo not found.')
        )


''''
DELETE todos/{id}/
'''


@todo_router.delete("/{todo_id}/", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):

    try:
        banco_dados.delete_todo(todo_id)

    except TodoModel.DoesNotExist:
        return JSONResponse(
            status_code=404,
            content=dict(error='Todo not found.')
        )

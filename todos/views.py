from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from todos.db.models import TodoModel
from fastapi import APIRouter
from .serializers import TodoCreateSerializer, TodoUpdateSerializer
from fastapi.responses import JSONResponse

todo_router = APIRouter()
database = TodosDBService()

'''
GET todos/

Aqui estou usando a aula e o git das meninas como base,peguei a lógica
do primeiro get no app
'''

@todo_router.get('/') #MÉTODO GET
def get_todos(): #DEFINIÇÃO DA FUNÇÃO PEGAR_TODOS
    alltodos = database.get_todos() #DECLARAÇÃO DE VARIÁVEL TODOS OS TODOS 
    #RECEBE DO BANCO DE DADOS GET_TODOS
    return alltodos

    #POSSO FAZER DESSA FORMA:
    #RETURN database.get_todos()


''''
GET todos/{id}/
'''
@todo_router.get('/{id}/')
def get_todo(id: str):
    try:
        todo = database.get_todo(id)
        return todo
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404, content=dict(
                                error='Todo not found.'))

'''
POST todos
'''


@todo_router.post('/', status_code=201)
def create_todo(todo: TodoCreateSerializer):
    return database.create_todo(todo)


                            
'''
PUT todos
'''


@todo_router.put('/{id}/')
def update_todo(id: str, todo: TodoUpdateSerializer):
    try:
        update = database.update_todo(id, todo)
        return update
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404, content=dict(
                            error='Todo not found.')
                            )

''''
DELETE todos/{id}/
'''


@todo_router.delete('/{id}/', status_code=204)
def delete_todo(id: str):
    try:
        delete = database.delete_todo(id)
        return delete
    except TodoModel.DoesNotExist:
        return JSONResponse(status_code=404, content=dict(
                                error='Todo not found.')
                            )

from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from fastapi import APIRouter
from .serializers import TodoCreateSerializer, TodoUpdateSerializer

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

'''
POST todos
'''

'''
PUT todos
'''

''''
DELETE todos/{id}/
'''

from common.serializers import ErrorSerializer
from todos.db.services import TodosDBService
from fastapi import APIRouter
from .serializers import TodoCreateSerializer, TodoSerializer, TodoUpdateSerializer

todo_router = APIRouter()

'''
GET todos/
'''
@todo_router.get('/todos/')
def get_title():
    user = TodoCreateSerializer.get_title()
''''
GET todos/{id}/
'''
@todo_router.get('/todos/{id}')
def get_user(id: str):
    user = TodoSerializer.get_user(id)

'''
POST todos
'''

'''
PUT todos
'''

''''
DELETE todos/{id}/
'''

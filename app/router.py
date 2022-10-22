from fastapi import APIRouter

from .endpoints import test, salary

api_router = APIRouter()

api_router.include_router(test.router, prefix='/test', tags=['test'])
api_router.include_router(salary.router, prefix='/salary', tags=['salary'])


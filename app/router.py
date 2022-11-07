from fastapi import APIRouter

from app.endpoints import salary

api_router = APIRouter()

api_router.include_router(salary.router, prefix='/salary', tags=['salary'])


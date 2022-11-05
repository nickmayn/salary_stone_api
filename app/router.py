from fastapi import APIRouter

from app.api.endpoints import salary

api_router = APIRouter()

api_router.include_router(salary.router, prefix='/salary', tags=['salary'])


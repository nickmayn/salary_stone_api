from fastapi import APIRouter

from app.endpoints import salary, metrics

api_router = APIRouter()

api_router.include_router(salary.router, prefix='/salary', tags=['salary'])
api_router.include_router(metrics.router, prefix='/metrics', tags=['metrics'])


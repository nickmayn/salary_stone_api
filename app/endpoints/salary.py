from fastapi.routing import APIRouter

from app.crud.delete import delete_salary
from ..crud.create import create_salary
from ..crud.search import search
from app.schema.salary import SalaryBase, SalarySearch

router = APIRouter()

@router.post('')
async def find(terms: dict):
    return(search(terms))

@router.post("/create")
async def create(payload: SalaryBase):
    create_salary(payload)
    
@router.post("/delete")
async def delete(payload: str):
    delete_salary(payload)

# @router.get("/similar")
# async def get_similar():
#     get_similar(payload: SalaryBase)
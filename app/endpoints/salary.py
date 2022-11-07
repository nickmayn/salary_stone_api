from fastapi.routing import APIRouter

from app.crud.delete import delete_salary
from app.crud.create import create_salary
from app.crud.search import search
from app.schema.salary import SalaryBase

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

@router.get('/test')
async def test():
    return ["50K", "60K", "70K", "80K", "90K", "100K", "110K", "120K"]

@router.post('/predict')
async def predict(jobdesc: str):
    if jobdesc.lower() == 'foo':
        return("100k")
    else:
        return("10k")

# @router.get("/similar")
# async def get_similar():
#     get_similar(payload: SalaryBase)
from fastapi.routing import APIRouter
from ..crud.create import create
from typing import List
from pandas import DataFrame

router = APIRouter()

@router.get("")
def ingest_table(df: DataFrame):
    for row in df:
        print(row)

@router.get("")
def create_salary(salary: List):
    return salary

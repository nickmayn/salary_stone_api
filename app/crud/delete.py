from .connect import es
from datetime import datetime

def delete_salary(id: str):
    es.delete(index="salaries",id=id)
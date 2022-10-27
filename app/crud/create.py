from .connect import es
from app.schema.salary import SalaryBase
from datetime import datetime
import uuid

def create_salary(salary: SalaryBase):
    doc = salary.dict()
    doc['ingest_time'] = datetime.now()
    es.index(index='salaries', id=str(uuid.uuid4()), document=doc)
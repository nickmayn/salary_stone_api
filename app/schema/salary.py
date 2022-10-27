from typing import List
from pydantic import BaseModel

class SalaryBase(BaseModel):
    job_title: str
    job_desc: str
    job_location: str
    job_sal_upper: float
    job_sal_lower: float
    job_sal_avg: float
    job_sector: str
    company: str
    company_size_lower: int
    company_size_upper: int
    company_hq_location: str
    company_ownership: str
    company_industry: str
    employee_degree: str
    employee_skills: List
    rating: float

class SalarySearch(BaseModel):
    job_title: str
    job_location: str
    job_salary_range: List
    company: str

from re import M
from fastapi.routing import APIRouter
from salary_stone.salary_extractor import Salary_Extractor
from salary_stone.skill_extractor import Skill_Extractor
from salary_stone.metrics import skill_freq, skill_salary_dist, similarity_measure
from salary_stone.skill_recommender import recommend
import pandas as pd

from app.crud.delete import delete_salary
from app.crud.create import create_salary
from app.crud.search import search
from app.schema.salary import SalaryBase

from ast import literal_eval

router = APIRouter()

salextractor = Salary_Extractor()
se = Skill_Extractor()
# TODO make this into where it reads from the database.
dat = pd.read_csv('processed_dat.csv')
# Format skills into format required for the method.
dat['skills'] = dat['skills'].apply(lambda r: literal_eval(r))


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
    try:
        ans = salextractor.extract_salary(jobdesc)
        return f'{round(ans[0])}K-{round(ans[1])}K'
    except:
        return ''

@router.post('/skills')
async def skills(jobdesc: str):
    
    skill_vec = se.extract_skills(jobdesc)
    skills, f = skill_freq(skill_vec=skill_vec, data=dat, extracted_scol='skills')
    dats = []
    for s, val in zip(skills, f):
        dats.append({'x': s, 'y':round(100*val)})
        
    return dats

@router.get('/skillsalbin')
async def skillsalbin(jobdesc: str):
    skill_vec = se.extract_skills(jobdesc)
    bins = skill_salary_dist(skill_vec = skill_vec, data=dat, extracted_salcol='salary_bins', extracted_scol='skills')
    res = []
    for key, val in bins.items():
        res.append({'name': key, 'data': val})
    return res

@router.get('/skillsim')
async def skillsim(jobdesc: str):
    skill_vec = se.extract_skills(jobdesc)
    res = similarity_measure(skill_vec=skill_vec, data=dat, topn=5, jobtitle_col='job_title_sim', extracted_scol='skills')
    score = []
    for val in res[0]:
        score.append(round(val*100))
    return ({'title': list(res[1]), 'score': score})

@router.get('/recommend')
async def rec(resume: str):
    print(resume)
    skillv = se.extract_skills(resume)
    skills, vals = recommend(skill_vec=skillv, data=dat, model=salextractor, extracted_scol='skills')
    res = []
    for s, val in zip(skills, vals):
        try: 
            tmp = round(100*val)
        except:
            tmp = val
        res.append({'recskills': s, 'recskillsalincrease': tmp})
    return(res)
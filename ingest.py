import pandas as pd
from requests import Session
from tqdm import tqdm
import json

df = pd.read_csv('~/Desktop/data_cleaned_2021.csv')

doc = {
  "job_title": "string",
  "job_desc": "string",
  "job_location": "string",
  "job_sal_upper": 0,
  "job_sal_lower": 0,
  "job_sal_avg": 0,
  "job_sector": "string",
  "company": "string",
  "company_size_lower": 0,
  "company_size_upper": 0,
  "company_hq_location": "string",
  "company_ownership": "string",
  "company_industry": "string",
  "employee_degree": "string",
  "employee_skills": [
    "string"
  ],
  "rating": 0
}

session = Session()
session.verify = False


for idx, row in tqdm(df.iterrows()):
    doc['job_title'] = row['Job Title']
    doc['job_desc'] = row['Job Description']
    doc['job_location'] = row['Location']
    doc['job_sal_upper'] = float(row['Upper Salary'])
    doc['job_sal_lower'] = float(row['Lower Salary'])
    doc['job_sal_avg'] = float(row['Avg Salary(K)'])
    doc['job_sector'] = row['Sector']
    doc['company'] = row['company_txt']
    try:
        csu = doc['company_size_upper'] = int(row['Size'].split('-')[1].strip().replace(' ', '').replace('+', ''))
    except:
        csu = None
    try:
        csl = int(row['Size'].split('-')[0].strip().replace(' ', '').replace('+', ''))
    except:
        csl = csu
    doc['company_size_upper'] = csu
    doc['company_size_lower'] = csl
    doc['company_hq_location'] = row['Headquarters']
    doc['company_ownership']= row['Type of ownership']
    doc['company_industry'] = row['Industry']
    doc['employee_degree'] = row['Degree']
    doc['rating'] = row['Rating']
    
    skills = []
    for skill in ['Python','spark', 'aws', 'excel', 'sql', 'sas', 'keras', 'pytorch', 'scikit', 'tensor', 'hadoop', 'tableau', 'bi', 'flink', 'mongo', 'google_an','job_title_sim']:
        if row[skill] == 1:
            skills.append(skill)
    doc['employee_skills'] = skills

    session.post(url='http://localhost:8000/salary/create', data=json.dumps(doc))

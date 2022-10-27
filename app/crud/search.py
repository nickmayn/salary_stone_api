from .connect import es
from app.schema.salary import SalarySearch

def search(q: SalarySearch):

    if len(q) == 0:
        query = {
            "match_all" : {}
        }
    else:
        query = {
            "bool": {
                "must": [{"range": {}}],
            }
        }
        for key, value in q.items():
            if value is not None:
                if key == 'job_salary_range':
                    query['bool']['must'][0]['range']['job_sal_avg'] = {
                        'gte': value[0],
                        'lte': value[1]
                    } 
                else:
                    query["bool"]["must"].append({'match': {str(key): value}})
    res = es.search(index="salaries", query=query)
    return res
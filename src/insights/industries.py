from typing import List, Dict

import csv

def get_unique_industries(path: str) -> List[str]:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        job_list = set()
        for row in reader:
            if(row['industry'] == ''):
                continue
            job_list.add(row['industry'])
        return list(job_list)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job['industry'] == industry]

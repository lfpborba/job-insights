from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
  with open(path, 'r') as file:
      reader = csv.DictReader(file)
      return list(reader)


def get_unique_job_types(path: str) -> List[str]:
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        return list({row['job_type'] for row in reader})


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job['job_type'] == job_type]

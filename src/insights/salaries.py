from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salaries = [
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isdigit()
    ]
    return max(max_salaries)


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salaries = [
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isdigit()
    ]
    return min(min_salaries)

def jobValidate(job: Dict) -> bool:
    notValid = True

    if not isinstance(job["min_salary"], (str, int)):
        notValid
    elif (
        isinstance(job["min_salary"], str) and not job["min_salary"].isdigit()
    ):
        notValid
    elif not isinstance(job["max_salary"], (str, int)):
        notValid
    elif (
        isinstance(job["max_salary"], str) and not job["max_salary"].isdigit()
    ):
        notValid
    else:
        notValid = False
    return notValid


def validateParams(job: Dict, salary: Union[int, str]) -> bool:
    notValid = True

    if jobValidate(job):
        notValid
    elif not isinstance(salary, (str, int)):
        notValid
    elif (
        isinstance(salary, str) and not salary.isdigit()
    ):
        notValid
    else:
        notValid = False
    return notValid

def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    match_result = False

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError
    elif validateParams(job, salary):
        raise ValueError
    else:
        if int(job["min_salary"]) > int(job["max_salary"]):
            raise ValueError
        elif int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
            match_result = True
    return match_result


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

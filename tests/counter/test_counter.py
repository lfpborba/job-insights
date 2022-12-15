import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("data/jobs.csv", "Python") == 1639


def test_counter_2():
    assert count_ocurrences("data/jobs.csv", "Java") == 676


def test_counter_3():
    assert count_ocurrences("data/jobs.csv", "javascript") == 122


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        count_ocurrences("data/jobs.json", "javascript")

import statistics
import time
from typing import Union

import pytest

MIN = 0
MAX = 4

@pytest.fixture(scope="session")
def data():
    # TODO: Parameterize for int and float types
    return range(MIN, MAX + 1, 1)

@pytest.fixture(scope="session", params=[int, float])
def max_val(request) -> Union[int, float]:
    return request.param(MAX)

@pytest.fixture(scope="session", params=[int, float])
def min_val(request) -> Union[int, float]:
    return request.param(MIN)

@pytest.fixture(scope="session")
def mean_val(data, request) -> Union[int, float]:
    return statistics.mean([float(val) for val in data])

@pytest.fixture(scope="session")
def stdev_val(data, request) -> Union[int, float]:
    return statistics.pstdev([float(val) for val in data])

@pytest.fixture(scope="function")
def slow():
    time.sleep(0.1)
    yield
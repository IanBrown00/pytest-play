"""

Run all parameterized versions of all tests in module:
>>> python3 -m pytest tests/test_mark.py

Run all parameterized versions of test:
>>> python3 -m pytest tests/test_mark.py::test_max

Run a single parameterized test (for one value of the fixture parameter):
>>> python3 -m pytest tests/test_mark.py::test_max[int]
>>> python3 -m pytest tests/test_mark.py::test_min[float]

Run only those tests marked as 'slow_test' (or inverse)
>>> python3 -m pytest tests/test_mark.py -m 'slow_test'
>>> python3 -m pytest tests/test_mark.py -m 'not slow_test'

"""

import pytest

import src.math_ops


def test_max(data, max_val):
    assert src.math_ops.mx(data) == max_val


def test_min(data, min_val):
    assert src.math_ops.mn(data) == min_val


@pytest.mark.slow_test
def test_mean(data, mean_val, slow):
    assert src.math_ops.mean(data) == mean_val


@pytest.mark.slow_test
def test_stdev(data, stdev_val, slow):
    assert src.math_ops.std(data) == stdev_val


@pytest.mark.xfail
def test_min_oops(data, max_val):
    assert src.math_ops.mn(data) == max_val


def test_min_oops(data, max_val):
    assert src.math_ops.mn(data) == 0

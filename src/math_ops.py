from math import sqrt
import statistics
from typing import Iterable, TypeVar

T = TypeVar('T')

def mean(values: Iterable[T]) -> T:
    return sum(values) / len(values)

def std(values: Iterable[T]) -> T:
    pop_mean = mean(values)
    return sqrt(sum([(float(v) - pop_mean) ** 2 for v in values])/len(values))

def mx(values: Iterable[T]) -> T:
    return max(values)

def mn(values: Iterable[T]) -> T:
    return min(values)


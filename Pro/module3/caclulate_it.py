from typing import Callable
import time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def calculate_it(func: Callable, *args):
    start_time = time.perf_counter()
    results = func(*args)
    end_time = time.perf_counter() - start_time
    return results, end_time


calculate_it(add, 1, 2, 3)

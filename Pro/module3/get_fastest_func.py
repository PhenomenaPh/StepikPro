import time
from typing import Callable, List


def measure_time(func, arg):
    start_time = time.perf_counter()
    func(arg)

    return time.perf_counter() - start_time


def get_the_fastest_func(funcs, arg):
    return min(funcs, key=lambda x: measure_time(x, arg=arg))

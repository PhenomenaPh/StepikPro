from typing import Iterable


def is_prime(number: int):
    return not any(i for i in range(2, int(number**0.5) + 1) if number % i == 0) or number < 2


def count_iterable(iterable: Iterable):
    return sum(1 for i in iterable)


def all_together(*args):
    return (j for i in args for j in i)


def interleave(*args):
    return (j for i in zip(*args) for j in i)

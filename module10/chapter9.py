from itertools import dropwhile, islice, compress

from typing_extensions import Iterable
from typing import Any, Callable


def drop_while_negative(iterable: Iterable):
    return dropwhile(lambda x: x < 0, iterable)


def drop_this(iterable: Iterable, obj: Any):
    return dropwhile(lambda x: x == obj, iterable)


def first_true(iterable: Iterable, predicate: Callable):
    return next(filter(predicate, iterable), None)


def take(iterable: Iterable, n: int):
    return islice(iterable, 0, n)


def take_nth(iterable: Iterable, n: int):
    return next(islice(iterable, n - 1, n), None)


def first_largest(iterable: Iterable, number: int):
    selectors = (i > number for i in iterable)

    for ix, val in enumerate(selectors):
        if val:
            return ix

    return -1


if __name__ == '__main__':
    iterator = iter([18, 21, 14, 72, 73, 18, 20])

    print(first_largest(iterator, 10))
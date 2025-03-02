from itertools import chain, repeat, starmap, pairwise, tee, zip_longest

from typing import Iterable


def sum_of_digits(iterable: Iterable):
    return sum(int(i) for i in chain.from_iterable(map(str, iterable)))


def is_rising(iterable: Iterable[int]):
    return not any(starmap(lambda x, y: x >= y, pairwise(iterable)))


def max_pair(iterable: Iterable):
    return max(map(sum, pairwise(iterable)))


def ncycles(iterable: Iterable, times: int):
    iterators = tee(iterable, times)

    for i in chain.from_iterable(iterators):
        yield i


# noinspection PyArgumentList
def grouper(iterable: Iterable, n: int):

    yield from zip_longest(*repeat(iter(iterable), n))


if __name__ == '__main__':
    from collections import namedtuple
    from itertools import groupby

    Person = namedtuple('Person', ['name', 'age', 'height'])

    persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
               Person('Mark', 71, 172), Person('Alex', 45, 193),
               Person('Jeff', 63, 193), Person('Ryan', 41, 184),
               Person('Ariana', 28, 158), Person('Liam', 69, 193)]

    sorted_persons = sorted(persons, key=lambda p: p.height)
    print(sorted_persons)


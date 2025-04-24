import random
from typing import Iterable


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

    def __iter__(self):
        yield from (self.x, self.y, self.z)


class DevelopmentTeam:
    def __init__(self):
        self.junie_workers = []
        self.senior_workers = []

    def add_junior(self, *args):
        for junie in args:
            self.junie_workers.append((junie, "junior"))

    def add_senior(self, *args):
        for senior in args:
            self.senior_workers.append((senior, "senior"))

    def __iter__(self):
        yield from self.junie_workers
        yield from self.senior_workers


class AttrsIterator:
    def __init__(self, obj: object):
        self.obj = obj
        self.attrs = [(k, v) for k, v in obj.__dict__.items()]
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.attrs):
            raise StopIteration
        return self.attrs[self.index]


class SkipIterator:
    def __init__(self, iterable: Iterable, n: int):
        self.iterable = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self.iterable)

        for _ in range(self.n):
            next(self.iterable, None)  # Не вызываем ошибку

        return val


class RandomLooper:
    def __init__(self, *args: Iterable):
        self.values = args

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        values = [elem for sublist in value for elem in sublist]
        random.shuffle(values)

        self._values = iter(values)

    def __iter__(self):
        return self

    def __next__(self):
        val = next(self.values)
        return val


class Peekable:
    def __init__(self, iterable: Iterable):
        self._iterable = iterable
        self.index = 0
        self.len_iter = len(list(self._iterable))

    def peek(self, default="default"):
        if self.index >= self.len_iter:
            if default != "default":
                return default
            else:
                raise StopIteration
        return self._iterable[self.index]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.len_iter - 1:
            raise StopIteration

        self.index += 1
        return self._iterable[self.index - 1]


class LoopTracker:
    def __init__(self, iterable: Iterable):
        self.iterable = iter(iterable)
        self._first = self._next = next(self.iterable, None)
        self._count, self._false_count = 0, 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._next is not None:
            self._count += 1
            self._last = self._next
            self._next = next(self.iterable, None)
            return self._last
        else:
            self._false_count += 1
            raise StopIteration

    @property
    def first(self):
        if self._first is not None:
            return self._first
        raise AttributeError("Исходный итерируемый объект пуст")

    @property
    def accesses(self):
        return self._count

    @property
    def empty_accesses(self):
        return self._false_count

    @property
    def last(self):
        if hasattr(self, "_last"):
            return self._last
        raise AttributeError("Последнего элемента нет")

    def is_empty(self):
        if self._next:
            return False
        return True

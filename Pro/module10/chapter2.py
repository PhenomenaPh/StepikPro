from typing import Callable, Iterable, Iterator
import random


def filterfalse(predicate: Callable | None, iterable):
    return filter(lambda x: not predicate(x) if predicate else not bool(x), iterable)


def transpose(matrix: list[list[int]]) -> list:
    transposed_matrix = zip(*matrix)
    return [list(i) for i in transposed_matrix]


# def get_min_max(data: list[Any]) -> tuple[int, int] | None:
#     if data:
#         max_val, min_val = max(data), min(data)
#         return data.index(min_val), data.index(max_val)
#     else:
#         return None


def starmap(func: Callable, iterable):
    return map(lambda x: func(*x), iterable)


def get_min_max(data: Iterator[int] | Iterable[int]):
    if data:
        data = iter(data)
        try:
            min_val, max_val = [next(data)] * 2

            for i in data:
                if i > max_val:
                    max_val = i
                elif i < min_val:
                    min_val = i
            return min_val, max_val
        except StopIteration:
            return None


def random_numbers(left: int, right: int):
    return iter(lambda: random.randint(a=left, b=right), -1)


if __name__ == "__main__":
    iterable = [6, 4, 2, 33, 19, 1]

    print(get_min_max(iterable))

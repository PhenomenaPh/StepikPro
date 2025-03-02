from itertools import product
from typing import Generator
from datetime import date, timedelta


def simple_sequence():
    current_value = 1

    while True:
        for _ in range(current_value):
            yield current_value

        current_value += 1


def alternating_sequence(count: int | None = None):
    n = 0

    while n != count:
        n += 1
        if n % 2:
            yield n
        else:
            yield n * -1


def primes(left: int, right: int) -> Generator:
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        else:
            return any(num % i == 0 for i in range(2, num**0.5 + 1))

    for i in range(left, right + 1):
        yield is_prime(i)


def reverse(sequence) -> Generator:
    for i in sequence[::-1]:
        yield i


def dates(start: date, count: int | None = None) -> Generator:
    n = 0

    while n != count:
        yield start

        try:
            start += timedelta(days=1)
        except OverflowError:
            return
        n += 1


def palindromes():
    def nums_gen(count: int = 1):
        while True:
            if str(count) == str(count)[::-1]:
                yield count
            count += 1

    yield from nums_gen()


def flatten(nested_lists: list[int | list]):
    for i in nested_lists:
        if isinstance(i, int):
            yield i
        else:
            yield from flatten(i)

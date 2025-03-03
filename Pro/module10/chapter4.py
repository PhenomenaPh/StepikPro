from collections.abc import Iterable
from itertools import product
import random


class Square:
    def __init__(self, n: int) -> None:
        self.n = n
        self.val = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.val == self.n:
            raise StopIteration
        else:
            self.val += 1
            return (self.val - 1) ** 2


class Fibonacci:
    def __init__(self) -> None:
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


class PowerOf:
    def __init__(self, number: int):
        self.number = number
        self.pow_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.pow_index += 1

        return self.number ** (self.pow_index - 1)


class DictItemsIterator:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.keys = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        current_key = next(self.keys)
        return current_key, self.data[current_key]


class CardDeck:
    def __init__(self) -> None:
        self.weights = tuple(range(2, 11)) + ("валет", "дама", "король", "туз")
        self.units = ("пик", "треф", "бубен", "червей")
        self.cards = product(self.units, self.weights)

    def __iter__(self):
        return self

    def __next__(self):
        current_card = next(self.cards)

        return f"{current_card[1]} {current_card[0]}"


class Cycle:
    def __init__(self, iterable: Iterable[str]):
        self.iterable = iter(iterable)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1

        try:
            return next(self.iterable)
        except StopIteration:
            self.iterable = iter(self.iterable)
            return next(self.iterable)


class RandomNumbers:
    def __init__(self, left: int, right: int, n: int):
        self.left = left
        self.right = right
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n:
            return random.randint(self.left, self.right)

        raise StopIteration


class Alphabet:
    def __init__(self, language: str) -> None:
        if language == "en":
            self.alphabet = range(ord("a"), ord("z") + 1)
        else:
            self.alphabet = range(ord("а"), ord("я") + 1)

        self.obj = iter(self.alphabet)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return chr(next(self.obj))

        except StopIteration:
            self.obj = iter(self.alphabet)


class Xrange:
    def __init__(self, start: int, end: int, step: int | float = 1) -> None:
        self.start = start - step

        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step

        if self.start >= self.end and self.step > 0:
            raise StopIteration
        elif self.start <= self.end and self.step < 0:
            raise StopIteration

        return self.start

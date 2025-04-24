import re
from typing import Iterable


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @staticmethod
    def from_diameter(cls, diameter: float) -> "Circle":
        return Circle(diameter / 2)


class Rectangle:
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side: float) -> "Rectangle":
        return cls(side, side)


class QuadraticPolynomial:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, iterable: Iterable[float]) -> "QuadraticPolynomial":
        return cls(*iterable)

    @classmethod
    def from_str(cls, s: str) -> "QuadraticPolynomial":
        return cls(*map(float, s.split()))


class Pet:
    pets = []

    def __init__(self, name: str) -> None:
        self.name = name
        self.__class__.pets.append(self)

    @classmethod
    def first_pet(cls) -> "Pet":
        if not cls.pets:
            return None
        return cls.pets[0]

    @classmethod
    def last_pet(cls) -> "Pet":
        if not cls.pets:
            return None
        return cls.pets[-1]

    @classmethod
    def num_pets(cls) -> int:
        return len(cls.pets)


class StrExtension:
    @staticmethod
    def remove_vowels(s: str) -> str:
        return "".join(c for c in s if c not in "aeiouyAEIOUY")

    @staticmethod
    def leave_alpha(s: str) -> str:
        return "".join(c for c in s if c.isalpha())

    @staticmethod
    def replace_all(s: str, old: str, new: str) -> str:
        for c in old:
            s = s.replace(c, new)
        return s


class CaseHelper:
    __snake_pattern = re.compile(r"^[a-z_]*$")
    __upper_camel_pattern = re.compile(r"^([A-Z][a-z]*)*$")

    @staticmethod
    def is_snake(s: str) -> bool:
        return CaseHelper.__snake_pattern.match(s) is not None

    @staticmethod
    def is_upper_camel(s: str) -> bool:
        return CaseHelper.__upper_camel_pattern.match(s) is not None

    @staticmethod
    def to_snake(s: str) -> str:
        return re.sub(r"(?<=\w)([A-Z])", r"_\1", s).lower()

    @staticmethod
    def to_upper_camel(s: str) -> str:
        return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s.capitalize())


if __name__ == "__main__":
    print(CaseHelper.is_snake("hello_world"))
    print(CaseHelper.is_upper_camel("HelloWorld"))
    print(CaseHelper.is_snake("asdfasf"))
    print(CaseHelper.is_upper_camel("asdfasf"))
    print(CaseHelper.to_upper_camel("bee_geek"))
    print(CaseHelper.to_snake("Beegeek"))
    print(CaseHelper.to_snake("BeeGeek"))

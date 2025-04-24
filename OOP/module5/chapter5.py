import datetime
import random
from collections.abc import Callable, Iterable
from functools import total_ordering


class FoodInfo:
    def __init__(self, proteins: int, fats: int, carbohydrates: int):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self) -> str:
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(
            self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates
        )

    def __sub__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(
            self.proteins - other.proteins, self.fats - other.fats, self.carbohydrates - other.carbohydrates
        )

    def __mul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)

    def __truediv__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)

    def __floordiv__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)

    def __mod__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return FoodInfo(self.proteins % other, self.fats % other, self.carbohydrates % other)


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return Vector(self.x / other, self.y / other)

    def __floordiv__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return Vector(self.x // other, self.y // other)

    def __rmul__(self, other):
        if not isinstance(other, int | float):
            return NotImplemented
        return Vector(self.x * other, self.y * other)


class SuperString:
    def __init__(self, string: str):
        self.string = string
        self.str_len = len(self.string)

    def __repr__(self) -> str:
        return f"SuperString({self.string})"

    def __str__(self) -> str:
        return self.string

    def __add__(self, other):
        if not isinstance(other, SuperString):
            return NotImplemented
        return SuperString(self.string + other.string)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return SuperString(self.string * other)

    def __rmul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        return SuperString(self.string * other)

    def __truediv__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        shift = self.str_len // other
        return SuperString(self.string[:shift])

    def __lshift__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other > self.str_len:
            return SuperString("")
        shift = self.str_len - other
        return SuperString(self.string[:shift])

    def __rshift__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other > self.str_len:
            return SuperString("")
        shift = other
        return SuperString(self.string[shift:])


class Time:
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

        self.total_time = hours * 60 + minutes

    def __repr__(self):
        return f"{((self.total_time // 60) % 24):02}:{(self.total_time % 60):02}"

    def __add__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        return self.__class__(self.hours + other.hours, self.minutes + other.minutes)

    def __iadd__(self, other):
        if not isinstance(other, Time):
            return NotImplemented
        self.total_time += other.total_time
        return self


class Queue:
    def __init__(self, *args):
        self.args = list(args)

    def add(self, *args):
        self.args.extend(args)

    def pop(self):
        try:
            return self.args.pop(0)
        except IndexError:
            return None

    def __str__(self):
        return f"{' -> '.join(map(str, self.args))}"

    def __eq__(self, value):
        if not isinstance(value, Queue):
            return NotImplemented
        return self.args == value.args

    def __ne__(self, value):
        if not isinstance(value, Queue):
            return NotImplemented
        return self.args == value.args

    def __add__(self, value):
        if not isinstance(value, Queue):
            return NotImplemented

        return self.__class__(*self.args + value.args)

    def __iadd__(self, value):
        if not isinstance(value, Queue):
            return NotImplemented

        self.args.extend(value.args)
        return self

    def __rshift__(self, n: int):
        if not isinstance(n, int):
            return NotImplemented
        return Queue(self.args[n:])


class Calculator:
    def __call__(self, a: int | float, b: int | float, operation: str):
        match operation:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                try:
                    return a / b
                except ZeroDivisionError:
                    raise ValueError("Деление на ноль невозможно")


class RaiseTo:
    def __init__(self, degree: int):
        self.degree = degree

    def __call__(self, x: int):
        return x**self.degree


class Dice:
    def __init__(self, sides: int) -> None:
        self.sides = sides

    def __call__(self):
        return random.randint(1, self.sides)


class QuadraticPolynomial:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: int):
        return self.a * x**2 + self.b * x + self.c


class Strip:
    def __init__(self, chars: str):
        self.chars = chars

    def __call__(self, string: str):
        return string.strip(self.chars)


class Filter:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, iterable: Iterable):
        return filter(self.func, iterable)


class DateFormatter:
    def __init__(self, country_code: "str"):
        self.country_code = country_code

    def __call__(self, d: datetime.date):
        match self.country_code:
            case "ru":
                return d.strftime("%d.%m.%Y")
            case "us":
                return d.strftime("%m-%d-%Y")
            case "ca":
                return d.strftime("%Y-%m-%d")
            case "br":
                return d.strftime("%d/%m/%Y")
            case "fr":
                return d.strftime("%d.%m.%Y")
            case "pt":
                return d.strftime("%d-%m-%Y")


class CountCalls:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


class CachedFunction:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.cache = {}

    def __call__(self, *arg):
        if arg not in self.cache:
            self.cache[arg] = self.func(*arg)

        return self.cache[arg]


class SortKey:
    def __init__(self, *args) -> None:
        self.args = args

    def __call__(self, class_val):
        return [getattr(class_val, i) for i in self.args]


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __bool__(self):
        return any([self.x, self.y])

    def __int__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

    def __float__(self):
        return float((self.x**2 + self.y**2) ** 0.5)

    def __complex__(self):
        return complex(self.x, self.y)


class Temperature:
    def __init__(self, temperature: int):
        self.temperature = temperature

    def __str__(self):
        return f"{round(self.temperature, 2)}°C"

    def to_fahrenheit(self):
        return self.temperature * 1.8 + 32

    @classmethod
    def from_fahrenheit(cls, temperature: int):
        temp_in_cls = 5 / 9 * (temperature - 32)
        return cls(temp_in_cls)

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


@total_ordering
class RomanNumeral:
    _roman_to_arabic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    _arabic_to_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def __init__(self, number: str):
        self.value = number
        self.arab_number = self.to_arabic(number)

    @classmethod
    def to_arabic(cls, value: str):
        arabic = 0
        len_of_val = len(value)

        for i in range(len_of_val):
            if (i + 1) < len_of_val and cls._roman_to_arabic[value[i]] < cls._roman_to_arabic[value[i + 1]]:
                arabic -= cls._roman_to_arabic[value[i]]
            else:
                arabic += cls._roman_to_arabic[value[i]]
        return arabic

    @classmethod
    def to_roman(cls, value: int):
        resulting_roman = ""

        for arabic, roman in cls._arabic_to_roman.items():
            if value != 0:
                while value >= arabic:
                    resulting_roman += roman
                    value -= arabic
            else:
                return resulting_roman

    def __str__(self):
        return self.value

    def __add__(self, other):
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        value = self.arab_number + other.arab_number

        return RomanNumeral(self.__class__.to_roman(value))

    def __sub__(self, other):
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        value = self.arab_number - other.arab_number
        return RomanNumeral(self.__class__.to_roman(value))

    def __eq__(self, other):
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self.arab_number == other.arab_number

    def __lt__(self, other):
        if not isinstance(other, RomanNumeral):
            return NotImplemented
        return self.arab_number < other.arab_number

    def __int__(self):
        return self.arab_number

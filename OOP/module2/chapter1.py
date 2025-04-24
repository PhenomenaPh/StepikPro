import datetime
import itertools
import json
import re
from collections.abc import Iterable
from functools import wraps
from typing import Any, Callable


def darts(num: int):
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(min(i, j, num - j + 1, num - i + 1), end=" ")
        print()


def check_brackets(s: str):
    regex_pattern = r"\(\)"
    while re.search(regex_pattern, s):
        s = re.sub(regex_pattern, "", s)

    return len(s) == 0


def inversions(values: list[int]):
    combinations = itertools.combinations(values, 2)

    filtered_comb = filter(lambda x: (x[0] > x[1]), combinations)

    return len(list(filtered_comb))


def pokemons() -> int:
    values = [i.strip() for i in open(0).readlines()]

    amount_of_duplicates = len(values) - len(set(values))
    return amount_of_duplicates


def jsonify(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)

        return json.dumps(value)

    return wrapper


def coordinates_validation():
    regex_pattern = r"^\((.*), (.*)\)"
    values = [i.strip() for i in open(0)]

    for value in values:
        vals: tuple[str, str] = re.search(pattern=regex_pattern, string=value).groups()

        if abs(float(vals[0])) <= 90 and abs(float(vals[1])) <= 180:
            print(True)
        else:
            print(False)


def quantify(iterable: Iterable, predicate: Callable):
    return sum(predicate(x) if predicate else bool(x) for x in iterable)


def pycon(year: int, month: int):
    dt = datetime.date(year, month, 1)

    days_to_thursday = (3 - dt.weekday()) % 7
    forth_thursday = dt + datetime.timedelta(days=days_to_thursday + 21)

    return forth_thursday.strftime("%d.%m.%Y")


def is_integer(string: str):
    try:
        return bool(int(string))
    except ValueError:
        return False


def is_decimal(string: str):
    try:
        return bool(float(string))
    except ValueError:
        return False


def is_fractional(string: str) -> bool:
    regex_pattern = r"^[-]?\d*\/[1-9][0-9]*"
    if bool(re.search(pattern=regex_pattern, string=string)):
        return True
    return False


def intersperse(iterable: Iterable, delimeter: int | str | float):
    if iterable:
        for idx, val in enumerate(iterable):
            if not idx:
                yield val
            else:
                yield delimeter
                yield val


def annual_return(start: int, percent: int, years: int):
    mod_percent = 1 + (percent / 100)

    for _ in range(1, years + 1):
        start *= mod_percent

        yield start


def pluck(data: dict, path: str, default: Any = None):
    keys = path.split(".")

    for key in keys:
        data = data.get(key, default)

    return data


def recviz(func):
    func_count = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal func_count

        func_params = [repr(arg) for arg in args]
        func_params.extend(f"{k}={repr(v)}" for k, v in kwargs.items())

        print(f"{'    ' * func_count}-> {func.__name__}({', '.join(func_params)})")
        func_count += 1

        value = func(*args, **kwargs)

        func_count -= 1
        print(f"{'    ' * func_count}<- {repr(value)}")

        return value

    return wrapper


# Or v-a-f to select whole function!
# Thats cool and easy to use!


# Quick demo of Zed's vim implemenation despite beings also in public beta


# 1. You have every basic vim command and move implemented: w for writing and / for filtering
# 2. Navigation is easy. Just use <c-w> + hjkl for moving between panes. Lets got to explorer <c-w>l. To get back just using <c-w>h
#   2.1 Even for terminal <c-w>j
#   2.2 What about Git? Same! <c-w>h
#   2.3 Now you are getting an idea of how well whole vim implementation was designed!
#
#  And more cool stuff like text-object. You can select whole function with <v+i+f> which stands for visual inside function

import datetime
import operator
from itertools import accumulate, count, cycle
from string import ascii_uppercase
from typing import Callable, Iterable


def parse_ranges(ranges: str):
    for i in ranges.split(","):
        a, b = map(int, i.split("-"))
        yield from range(a, b + 1)


def filter_names(names: list[str], ignore_char: str, max_games: int):
    ignore_char_lower = ignore_char.lower()

    names_without_char = (i for i in names if not i.lower().startswith(ignore_char_lower))
    names_without_digit = (i for i in names_without_char if not any(j.isdigit() for j in i))

    for _ in range(max_games):
        try:
            yield next(names_without_digit)
        except StopIteration:
            break


def invest(file_name: str) -> int:
    with open(file_name, "r", encoding="utf-8") as file:
        file_lines = (line for line in file)
        line_values = (line.rstrip().split(",") for line in file_lines)
        headers = next(line_values)

        values_dict = (dict(zip(headers, data)) for data in line_values)

        filtered_values = (int(line["raisedAmt"]) for line in values_dict if line["round"] == "a")

        return sum(filtered_values)


def years_days(year: int):
    init_day = datetime.date(year, 1, 1).toordinal()
    final_day = datetime.date(year + 1, 1, 1).toordinal()

    for i in range(init_day, final_day):
        yield datetime.date.fromordinal(i).isoformat()


def nonempty_lines(file: str):
    with open(file, "r", encoding="utf-8") as file:
        file_lines = (line.strip() for line in file if line.strip())
        filtered_lines = ("..." if len(line) > 25 else line for line in file_lines)
        yield from filtered_lines


def txt_to_dict():
    init_dict = {}

    with open("planets.txt", "r", encoding="utf-8") as file:
        file_lines = (line for line in file)

        for line in file_lines:
            if line.strip() != "":
                key, val = line.strip().split(" = ")
                init_dict |= {key: val}
            else:
                yield init_dict
                init_dict = {}

        yield init_dict


def unique(iterable: Iterable):
    init_dict = {}

    for i in iterable:
        init_dict[i] = init_dict.get(i, 0) + 1

    unique_values = (k for k in init_dict.keys())

    yield from unique_values


def stop_on(iterable, obj):
    iter_obj = iter(iterable.__next__, obj)
    yield from iter_obj


def with_previous(iterable):
    previous = None

    for i in iterable:
        yield i, previous
        previous = i


def pairwise(iterable):
    iterator = iter(iterable)
    i = next(iterator)

    while i is not None:
        i, prev = next(iterator, None), i
        yield prev, i


def around(iterable):
    iterator = iter(iterable)

    previous = None
    i = next(iterator, None)

    while i is not None:
        next_val = next(iterator, None)
        yield previous, i, next_val

        previous, i = i, next_val


def tabulate(func: Callable):
    for i in count(1):
        yield func(i)


def factorials(n: int):
    return accumulate(range(1, n + 1), operator.mul, initial=1)


def alnum_sequence():
    for item in cycle(zip(range(1, 27), ascii_uppercase)):
        yield from item


def roundrobin(*args: Iterable):
    iterators = [iter(i) for i in args]

    current_index = 0
    while iterators:
        try:
            yield next(iterators[current_index])
            current_index = (current_index + 1) % len(iterators)

        except StopIteration:
            iterators.remove(iterators[current_index])
            current_index = current_index % len(iterators) if iterators else 0


if __name__ == "__main__":
    numbers = [1, 2, 3]
    letters = iter('beegeek')

    print(*roundrobin(numbers, letters))

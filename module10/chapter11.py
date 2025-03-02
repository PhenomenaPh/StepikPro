from collections import namedtuple
from itertools import groupby
from typing import Iterable
from itertools import groupby


def group_words(iterable: Iterable[str]):
    sorted_values = sorted(iterable, key=len)

    grouped_words = groupby(sorted_values, key=len)

    for length, words in grouped_words:
        print(f"{length} -> {', '.join(list(sorted(words)))}")


def exercise_preference(iterable: Iterable[tuple[str, str, int]]):
    sorted_taskts = sorted(iterable, key=lambda x: (x[0], x[2], x[1]))
    grouped_values = groupby(sorted_taskts, key=lambda x: x[0])

    for value, main_task in grouped_values:
        print(f'{value}:')
        for sub_task in main_task:
            print(f'\t{sub_task[2]}. {sub_task[1]}')
        print()


def group_anagrams(words: list[str]):
    sorted_words = groupby(sorted(words, key=sorted), key=sorted)

    return [tuple(i[1]) for i in sorted_words]


def ranges(numbers: Iterable[int]):
    final_list = []
    grouped_values = groupby(numbers, lambda x: numbers.index(x) - x)

    for key, group in grouped_values:
        list_group = list(group)
        final_list.append((list_group[0], list_group[-1]))

    return final_list


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 7, 8, 10]
    print(ranges(numbers))

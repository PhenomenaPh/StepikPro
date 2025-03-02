from typing import Callable
from string import ascii_lowercase, ascii_uppercase, digits


def hash_as_key(objects: list[int]):
    storage: dict = {}

    for i in objects:
        hash_val = hash(i)

        if hash_val in storage:
            current = storage[hash_val]
            if not isinstance(current, list):
                storage[hash_val] = [storage.get(hash_val)] + [i]
            else:
                storage[hash_val] = storage[hash_val].append(i)
        else:
            storage[hash_val] = i

    return storage


def collection() -> None:
    input_val = eval(input())

    if isinstance(input_val, list):
        print(input_val[-1])
    elif isinstance(input_val, tuple):
        print(tuple[0])
    else:
        print(len(input_val))


def math_code():
    values = [eval(i) for i in open(0)]
    print(max(values))


def min_max():
    f = input().replace("x", "({x})")
    a, b = map(int, input().split())

    values = [eval(f.format(x=x)) for x in range(a, b + 1)]
    print(f"Минимальное значениe функции {f} на отрезке [{a}; {b}] равно {min(values)}")
    print(f"Максимальное значениe функции {f} на отрезке [{a}; {b}] равно {max(values)}")


def fibonachi(n: int) -> int:
    if n in [1, 2]:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


def print_operation_table(func: Callable, rows: int, cols: int):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print(func(i, j), end=" ")
        print()


def verification(login: str, password: str, success: Callable, failure: Callable):
    d = {
        0: "в пароле нет ни одной буквы",
        1: "в пароле нет ни одной заглавной буквы",
        2: "в пароле нет ни одной строчной буквы",
        3: "в пароле нет ни одной цифры",
    }

    if not any(filter(lambda x: x in ascii_lowercase + ascii_uppercase, password)):
        return failure(login, d[0])
    elif not any(filter(lambda x: x in ascii_uppercase, password)):
        return failure(login, d[1])
    elif not any(filter(lambda x: x in ascii_lowercase, password)):
        return failure(login, d[2])
    elif not any(filter(lambda x: x in digits, password)):
        return failure(login, d[3])
    else:
        success(login)







print_operation_table(lambda a, b: a * b, 5, 5)

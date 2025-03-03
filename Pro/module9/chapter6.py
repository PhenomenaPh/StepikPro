from typing import TypedDict
from functools import wraps


class GradesInfo(TypedDict):
    name: str
    grades: list[int]


def get_digits(number: int | float) -> list[int]:
    return [int(i) for i in str(number) if i.isdigit()]


def top_grade(grades: GradesInfo) -> dict[str, str | int]:
    return {"name": grades["name"], "top_grade": max(grades["grades"])}


def cyclic_shift(numbers: list[int | float], step: int) -> None:
    step %= len(numbers)
    #
    # numbers[:] = numbers[-step:] + numbers[:-step]

    for i in range(step):
        numbers.insert(0, numbers.pop)


def matrix_to_dict(matrix: list[list[float | int]]) -> dict[int, list[int | float]]:
    dict_to_return = {idx + 1: val for idx, val in enumerate(matrix)}

    return dict_to_return


def sandwich(func):
    def wrapper(*args, **kwargs):
        print("---- Верхний ломтик хлеба ----")
        a = func(*args, **kwargs)
        print("---- Нижний ломтик хлеба ----")
        return a

    return wrapper


def new_princt(func):
    def wrapper(*args, **kwargs):
        args = [str(i).upper() for i in args]
        kwargs = {k: v.upper() for k, v in kwargs.items()}

        return func(*args, **kwargs)

    return wrapper


def do_twice(func):
    def wrapper(*args, **kwargs):
        values = [func(*args, **kwargs) for i in range(2)]

        return values[0]

    return wrapper


def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)

    return wrapper


def exception_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs), "Функция выполнилась без ошибок"
        except Exception:
            return None, "При вызове функции произошла ошибка"

    return wrapper


def takes_positive(func):
    def wrapper(*args, **kwargs):
        for i in [*args, *kwargs.values()]:
            if not isinstance(i, int):
                raise TypeError
            elif i <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return wrapper


def square(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        return a**2

    return wrapper()


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_return = func(*args, **kwargs)
        if not isinstance(func_return, str):
            raise TypeError
        else:
            return func_return

    return wrapper


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов {trace(func)} с аргументами {args}, {kwargs}")
        a = func(*args, **kwargs)
        print(f"TRACE: возвращаемое значение {trace(func)}(): {a}")

    return wrapper


if __name__ == "__main__":

    @sandwich
    def beegeek():
        return "beegeek"

    print(beegeek())

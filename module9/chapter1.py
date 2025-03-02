from typing import Any


def non_negative_even(numbers: list[int]) -> bool:
    return all([(i % 2 == 0) and (i >= 0) for i in numbers])


def is_greater(lists: list[list[int]], number: int) -> bool:
    condition = any(sum(i) > number for i in lists)
    return condition


def custom_isinstance(objects: Any, typeinfo) -> int:
    num_of_instance = sum([isinstance(i, typeinfo) for i in objects])
    return num_of_instance


def my_pow(number: int):
    pow_sum = sum([int(val) ** (idx + 1) for idx, val in enumerate(str(number))])
    return pow_sum


def zip_longest(*args: list[int | str], fill: str | None = None):
    max_len = max(map(len, args))
    modif_vars = [i + [fill] * (max_len - len(i)) for i in args]

    return list(zip(*modif_vars))


def custom_sort(input_val: str) -> str:
    sorted_items = sorted(
        input_val,
        key=lambda x: (
            (0, x)
            if x.islower()
            # lowercase first
            else (1, x)
            if x.isupper()
            # uppercase second
            else (3, int(x))
            if x.isdigit() and int(x) % 2 != 0
            else (4, x)  # fallback
        ),
    )

    return "".join(sorted_items)


if __name__ == "__main__":
    input_val = input()
    print(custom_sort(input_val))

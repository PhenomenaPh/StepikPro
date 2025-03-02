def numbers_sum(elems) -> int | float:
    """
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """

    filtered_values = list(filter(lambda x: isinstance(x, (int, float)), elems))

    if not any(filtered_values):
        return 0
    else:
        return sum(filtered_values)


def polynom(x: float):
    value = x**2 + 1
    if 'values' not in polynom.__dict__:
        polynom.values = set()

    polynom.values.add(value)
    return value

def remove_marks(text: str, marks: str) -> str:
    remove_marks.__dict__.setdefault('count', 0)

    refactored_text = text.translate(str.maketrans("", "", marks))
    remove_marks.count += 1

    return refactored_text


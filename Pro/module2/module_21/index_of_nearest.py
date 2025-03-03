def index_of_nearest(numbers: list, number: int) -> int:
    if len(numbers) == 0:
        return -1
    minimal_value = min(numbers, key=lambda x: abs(number - x))
    return numbers.index(minimal_value)

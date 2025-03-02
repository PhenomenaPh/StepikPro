def same_parity(numbers: list) -> list:

    if len(numbers) == 0:
        return numbers

    n = numbers[0] % 2

    return [number for number in numbers if number % 2 == n]

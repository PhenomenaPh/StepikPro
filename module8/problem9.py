def range_sum(numbers: list[int], start: int, end: int):
    if start == end:
        print("start", numbers[start])
        return numbers[end]
    else:
        print("start", numbers[start])
        return numbers[start] + range_sum(numbers, start + 1, end)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))

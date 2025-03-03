def get_biggest(numbers: list):
    if numbers:
        max_len = len(str(max(numbers)))
        sorted_list = sorted(map(str, numbers), key=lambda x: x * max_len, reverse=True)
        return int("".join(sorted_list))
    else:
        return -1


print(get_biggest([7, 71, 72]))

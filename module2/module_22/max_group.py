def max_group():
    values = [str(i) for i in range(1, int(input()) + 1)]
    values_pairs = {}

    for value in values:
        sum_value = sum(map(int, value))
        values_pairs[sum_value] = values_pairs.get(sum_value, []) + [value]

    return len(max(values_pairs.values(), key=len))


print(max_group())

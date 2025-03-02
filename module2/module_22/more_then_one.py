def best_values():
    values = list(map(int, input().split()))
    value_dict = {value: values.count(value) for value in set(values)}

    print(
        " ".join([str(value) for value in value_dict.keys() if value_dict[value] > 1])
    )


best_values()

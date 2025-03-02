from typing import Hashable


def recursive_num(nested_lists: list):
    total = 0

    for value in nested_lists:
        if isinstance(value, int):
            total += value
        else:
            total += recursive_num(value)

    return total


def get_value(nested_dicts: dict, key: Hashable):
    if key in nested_dicts.keys():
        return nested_dicts.get(key, None)

    for value in nested_dicts.values():
        if isinstance(value, dict):
            if (key_val := get_value(value, key)) is not None:
                return key_val


def linear(nested_lists: list[int | list]):
    last_list: list[int | list] = []

    for i in nested_lists:
        if isinstance(i, int):
            last_list.append(i)
        else:
            last_list.extend(linear(i))

    return last_list


def get_all_values(nested_dicts: dict, key: Hashable):
    values = set()

    if key in nested_dicts:
        values.add(nested_dicts[key])

    for value in nested_dicts.values():
        if isinstance(value, dict):
            values.update(get_all_values(value, key))

    return values


def dict_travel(nested_dicts: dict | int | str, path: str = ""):
    for k, v in sorted(nested_dicts.items(), key=lambda x: x[0]):
        if not isinstance(v, dict):
            print(f"{path}{k}: {v}")
        else:
            cur_path = path + k + "."
            dict_travel(v, cur_path)


if __name__ == "__main__":
    data = {"a": 1, "b": 5, "g": {"d": 1, "e": 4, "f": {"b": 3, "a": 4}}, "c": 3}

    dict_travel(data)

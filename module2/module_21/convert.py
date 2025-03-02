def convert(string: str) -> bool:

    value_sum = sum(1 if value.islower() else -1 for value in string if value.isalpha())

    if value_sum >= 0:
        return string.lower()
    else:
        return string.upper()

def is_good_password(string: str):
    if len(string) < 9:
        return False
    elif (
        not any(char.isdigit() for char in string)
        or not any(char.islower() for char in string)
        or not any(char.isupper() for char in string)
    ):
        return False
    return True

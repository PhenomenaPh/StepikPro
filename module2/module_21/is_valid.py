def is_valid(password: str) -> bool:

    possible_values = [str(i) for i in range(0, 10)]

    if (
        all([value in possible_values for value in password])
        and str(" ") not in password
        and len(password) in [4, 5, 6]
    ):
        return True
    return False

class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str):
    has_upper = False
    has_lower = False
    has_letter = False
    has_digit = False

    if len(string) < 9:
        raise LengthError

    for char in string:
        if char.isalpha():
            has_letter = True

            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
        else:
            if char.isdigit():
                has_digit = True

    if not has_letter or not (has_upper and has_lower):
        raise LetterError

    elif not has_digit:
        raise DigitError

    return True

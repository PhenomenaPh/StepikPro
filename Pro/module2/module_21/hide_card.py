def hide_card(password: str) -> str:
    corrected_password = password.replace(" ", "")
    last_4_digits = corrected_password[-4:]

    return "*" * 12 + last_4_digits


card = "3456 9012 5678 1234"

print(hide_card(card))

def get_id(names: list[str], name: str) -> int:
    if not isinstance(name, str):
        raise TypeError("Имя не является строкой")
    elif not name.istitle() or not name.isalpha():
        raise ValueError("Имя не является корректным")
    return len(names) + 1

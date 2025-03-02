from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(day=day, month=month, year=year)
        return True
    except Exception:
        return False

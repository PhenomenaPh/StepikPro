import calendar
from datetime import datetime, timedelta


def get_all_mondays(year: int) -> list[datetime.date]:
    """
    Calculating all mondays in specified year
    :param year:
    :return list[datetime.date]:

    >>> get_all_mondays(2021)[0]
    datetime.date(2021, 1, 4)
    >>> get_all_mondays(2021)[-1]
    datetime.date(2021, 12, 27)
    """
    first_day = datetime(year, month=1, day=1).date()

    current_monday = first_day + timedelta(days=(7 - first_day.weekday()) % 7)

    days = []
    while current_monday.year == year:
        days.append(current_monday)
        current_monday += timedelta(days=7)

    return days

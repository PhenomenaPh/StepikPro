from datetime import datetime, timedelta

year_obj = int(input())


def get_third_thursday(year: int) -> None:
    """
    Calculating all mondays in specified year
    :param year:
    :return list[datetime.date]:
    """
    for month in range(1, 13):
        first_day = datetime(year, month, 1)
        third_thursday = first_day + timedelta((3 - first_day.weekday()) % 7 + 15)
        print(third_thursday)


get_third_thursday(year_obj)

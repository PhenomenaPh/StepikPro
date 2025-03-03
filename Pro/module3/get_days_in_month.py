import calendar
from datetime import datetime, date, timedelta


def get_days_in_month(year_obj: int, month_name: str) -> list[date]:
    """
    Calculating list of dates
    :param year_obj: year value
    :param month_name: month full name
    :return: list of datetime.date values

    >>> days = get_days_in_month(2021, 'December')
    >>> days[0]
    datetime.date(2021, 12, 1)
    >>> days[-1]
    datetime.date(2021, 12, 31)
    """
    month_num = list(calendar.month_name).index(month_name)
    month_count = calendar.monthrange(year_obj, month_num)[1]
    start_dt = datetime(year_obj, month=month_num, day=1)

    return [(start_dt + timedelta(days=i)).date() for i in range(month_count)]

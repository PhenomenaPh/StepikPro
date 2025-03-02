from datetime import datetime
from typing import List


def fill_up_missing_dates(dates_list: List[str]) -> list:
    """
    Fill up missing dates in a given list of dates.

    :param dates_list: A list of strings representing dates in the format '%d.%m.%Y'.
    :return: A list of strings representing all dates between the minimum and maximum dates in the input list, inclusive

    Example:
    >>> fill_up_missing_dates(['01.01.2022', '03.01.2022', '05.01.2022'])
    ['01.01.2022', '02.01.2022', '03.01.2022', '04.01.2022', '05.01.2022']
    >>> fill_up_missing_dates(['01.11.2021', '04.11.2021', '09.11.2021', '15.11.2021'])
    ['01.11.2021', '02.11.2021', '03.11.2021', '04.11.2021', '05.11.2021', '06.11.2021', '07.11.2021', '08.11.2021', \
'09.11.2021', '10.11.2021', '11.11.2021', '12.11.2021', '13.11.2021', '14.11.2021', '15.11.2021']
    """

    pattern = "%d.%m.%Y"
    dates_list = list(map(lambda x: datetime.strptime(x, pattern), dates_list))
    min_date, max_date = map(
        lambda x: datetime.toordinal(x), [min(dates_list), max(dates_list)]
    )

    return [
        datetime.strftime(datetime.fromordinal(dt), pattern)
        for dt in range(min_date, max_date + 1)
    ]


if __name__ == "__main__":
    dates = ["01.11.2021", "07.11.2021", "04.11.2021", "03.11.2021"]
    fill_up_missing_dates(dates)

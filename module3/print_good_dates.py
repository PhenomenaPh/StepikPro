from datetime import date
from typing import List


def print_good_dates(dates_list: List[date]):
    print(
        *[
            value.strftime("%B %d, %Y")
            for value in sorted(dates_list)
            if value.year == 1992 and (value.month + value.day) == 29
        ],
        sep="\n",
    )


if __name__ == "__main__":
    dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
    print_good_dates(dates)

from datetime import date


def saturdays_between_two_dates(start: date, end: date):
    if start > end:
        start, end = end, start

    saturdays = [
        date.fromordinal(value)
        for value in range((start.toordinal()), end.toordinal() + 1)
        if date.fromordinal(value).weekday() == 5
    ]
    return len(saturdays)


if __name__ == "__main__":
    date1 = date(2021, 11, 1)
    date2 = date(2021, 11, 22)

    print(saturdays_between_two_dates(date1, date2))

from datetime import date, timedelta


# def get_date_range(start: date, end: date):
#     if start > end:
#         return []
#     else:
#         return [start + timedelta(days=i) for i in range((end - start).days + 1)]


def get_date_range(start: date, end: date):

    return [
        date.fromordinal(value)
        for value in range(start.toordinal(), end.toordinal() + 1)
    ]


if __name__ == "__main__":
    date1 = date(2021, 10, 6)
    date2 = date(2021, 10, 5)

    print(*get_date_range(date1, date2), sep="\n")

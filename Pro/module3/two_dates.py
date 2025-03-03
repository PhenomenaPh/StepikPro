from datetime import date


def min_date(date1: date, date2: date) -> date:

    if date1 > date2:
        chosen_date = date2
    else:
        chosen_date = date1

    return chosen_date.strftime("%d-%m (%Y)")


if __name__ == "__main__":
    date_1, date_2 = map(date.fromisoformat, [input(), input()])
    print(min_date(date_1, date_2))

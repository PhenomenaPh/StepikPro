from datetime import datetime, timedelta


# TODO: - redo with abs syntaxix


def compare_date(first_date: datetime, second_date: datetime):

    if second_date < first_date:
        first_date, second_date = second_date, first_date

    return (second_date - first_date).days


def neighbours():
    pattern = "%d.%m.%Y"
    dates = list(map(lambda x: datetime.strptime(x, pattern), input().split()))

    return [compare_date(dates[i], dates[i + 1]) for i in range(len(dates) - 1)]


if __name__ == "__main__":
    print(neighbours())

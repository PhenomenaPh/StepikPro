from datetime import datetime, timedelta


def productive():
    pattern = "%d.%m.%Y"

    current_date = datetime.strptime(input(), pattern)

    for i in range(2, 12):
        print(current_date.strftime(pattern))
        current_date += timedelta(days=i)


if __name__ == "__main__":
    productive()

from datetime import date, datetime, timedelta


def num_of_sundays():
    dt = date(year=int(input()), month=12, day=31)

    print(dt.strftime("%U"))


if __name__ == "__main__":
    num_of_sundays()

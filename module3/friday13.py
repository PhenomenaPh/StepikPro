from datetime import date, timedelta


def week_13():
    weeks = [0] * 7
    for year_dt in range(1, 10000):
        for month_dt in range(1, 13):
            weeks[date(year=year_dt, month=month_dt, day=13).weekday()] += 1
    return weeks


if __name__ == "__main__":
    print(*week_13(), sep="\n")

from datetime import date, datetime, timedelta


def next_prev_dt(dt: datetime):
    next_date, prev_date = map(
        lambda x: datetime.strftime(x, "%d.%m.%Y"),
        [dt + timedelta(days=1), dt - timedelta(days=1)],
    )

    return prev_date, next_date


if __name__ == "__main__":
    current_date = datetime.strptime(str(input()), "%d.%m.%Y")
    print(*next_prev_dt(current_date), sep="\n")

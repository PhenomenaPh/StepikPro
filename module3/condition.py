from datetime import datetime, timedelta


def condition_dt():
    pattern = "%d.%m.%Y"
    start_dt, end_dt = list(
        map(lambda x: datetime.strptime(x, pattern), [input() for _ in range(2)])
    )

    while (start_dt.month + start_dt.day) % 2 == 0:
        start_dt += timedelta(days=1)

    while start_dt <= end_dt:
        if start_dt.weekday() != 0 and start_dt.weekday() != 3:
            print(start_dt.strftime(pattern))

        start_dt += timedelta(days=3)


condition_dt()

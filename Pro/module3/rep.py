from datetime import datetime, date, time, timedelta


def working_hours() -> None:
    pattern = "%H:%M"
    start_time, end_time = [datetime.strptime(input(), pattern) for _ in range(2)]

    while start_time + timedelta(minutes=45) <= end_time:

        print(
            f"{start_time.strftime(pattern)} - {(start_time + timedelta(minutes=45)).strftime(pattern)}"
        )
        start_time += timedelta(minutes=55)


if __name__ == "__main__":
    working_hours()

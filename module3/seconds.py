from datetime import datetime, timedelta


def get_seconds():

    pattern = "%H:%M:%S"
    dt = datetime.strptime(input(), pattern)

    return timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second).seconds


if __name__ == "__main__":
    print(get_seconds())

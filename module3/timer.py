from datetime import datetime, timedelta


def timer():
    pattern = "%H:%M:%S"
    current_time = datetime.strptime(input(), pattern)
    seconds = int(input())

    timer_time = current_time + timedelta(seconds=seconds)

    return timer_time.strftime(pattern)


if __name__ == "__main__":
    print(timer())

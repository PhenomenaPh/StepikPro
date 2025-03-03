from datetime import datetime, timedelta


def shop_hours():
    pattern = "%d.%m.%Y %H:%M"

    current_date = datetime.strptime(input(), pattern)
    dt_delta = timedelta(hours=current_date.hour, minutes=current_date.minute)

    if current_date.weekday() < 5 and timedelta(hours=9) <= dt_delta <= timedelta(
        hours=21
    ):
        print((timedelta(hours=21) - dt_delta).seconds // 60)
    elif current_date.weekday() >= 5 and timedelta(hours=10) <= dt_delta <= timedelta(
        hours=18
    ):
        print((timedelta(hours=18) - dt_delta).seconds // 60)
    else:
        print("Магазин не работает")


shop_hours()

from datetime import datetime, timedelta
from typing import List


def parse_dates(dts) -> tuple:

    dates = tuple(map(lambda x: datetime.strptime(x, "%d.%m.%Y"), dts.split("-")))
    return dates if len(dates) > 1 else dates * 2


def check_availability(booked_date, booking_date):
    return booked_date[1] < booking_date[0] or booked_date[0] > booking_date[1]


def is_available_date(booked_dates, booking_dates):
    booking_dts = parse_dates(booking_dates)

    for dt in booked_dates:
        if not check_availability(parse_dates(dt), booking_dts):
            return False
    return True

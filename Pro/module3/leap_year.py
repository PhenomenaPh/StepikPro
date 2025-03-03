import calendar


def is_leap_year():
    for _ in range(int(input())):
        year = int(input())
        print(calendar.isleap(year))


is_leap_year()

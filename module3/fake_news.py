from datetime import datetime


def choose_plural(amount: int, declensions: tuple):
    if amount % 10 == 1 and amount % 100 != 11:
        return f"{amount} {declensions[0]}"
    elif amount % 10 in [2, 3, 4] and amount % 100 not in [12, 13, 14]:
        return f"{amount} {declensions[1]}"
    else:
        return f"{amount} {declensions[2]}"


def fake_news_announcment(dt: str):

    paradigms = (
        ("день", "дня", "дней"),
        ("час", "часа", "часов"),
        ("минута", "минуты", "минут"),
    )  # Склонение слов

    pattern = "%d.%m.%Y %H:%M"
    announce_dt = datetime(year=2022, month=11, day=8, hour=12)
    current_dt = datetime.strptime(dt, pattern)

    time_left = announce_dt - current_dt

    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = time_left.seconds % 3600 // 60

    days_str = choose_plural(days, paradigms[0])
    hours_str = choose_plural(hours, paradigms[1])
    minutes_str = choose_plural(minutes, paradigms[2])

    result_str = "До выхода курса осталось: "

    if current_dt >= announce_dt:
        return "Курс уже вышел!"

    if days:
        result_str += days_str
        if hours:
            result_str += " и " + hours_str

    elif hours:
        result_str += hours_str
        if minutes:
            result_str += " и " + minutes_str

    elif minutes:
        result_str += minutes_str

    return result_str


if __name__ == "__main__":
    assert (
        fake_news_announcment("16.11.2021 06:30")
    ) == "До выхода курса осталось: 357 дней и 5 часов"
    assert (
        fake_news_announcment("06.11.2022 12:00")
    ) == "До выхода курса осталось: 2 дня"
    assert (
        fake_news_announcment("08.11.2022 10:30")
    ) == "До выхода курса осталось: 1 час и 30 минут"
    assert (
        fake_news_announcment("08.11.2022 09:00")
    ) == "До выхода курса осталось: 3 часа"
    assert (
        fake_news_announcment("08.11.2022 11:40")
    ) == "До выхода курса осталось: 20 минут"
    assert (fake_news_announcment("08.11.2022 12:15")) == "Курс уже вышел!"
    assert (
        fake_news_announcment("08.11.2022 01:00")
    ) == "До выхода курса осталось: 11 часов"
    assert (
        fake_news_announcment("07.11.2022 15:00")
    ) == "До выхода курса осталось: 21 час"
    assert (
        fake_news_announcment("18.10.2022 12:00")
    ) == "До выхода курса осталось: 21 день"
    assert (
        fake_news_announcment("17.10.2022 12:00")
    ) == "До выхода курса осталось: 22 дня"
    assert (
        fake_news_announcment("09.10.2022 12:00")
    ) == "До выхода курса осталось: 30 дней"
    assert (
        fake_news_announcment("06.10.2021 12:35")
    ) == "До выхода курса осталось: 397 дней и 23 часа"
    assert (
        fake_news_announcment("17.12.2021 23:17")
    ) == "До выхода курса осталось: 325 дней и 12 часов"
    assert (
        fake_news_announcment("28.06.2022 17:54")
    ) == "До выхода курса осталось: 132 дня и 18 часов"
    assert (
        fake_news_announcment("14.05.2000 18:43")
    ) == "До выхода курса осталось: 8212 дней и 17 часов"
    assert (fake_news_announcment("08.11.2022 12:00")) == "Курс уже вышел!"
    assert (
        fake_news_announcment("08.11.2022 11:39")
    ) == "До выхода курса осталось: 21 минута"
    assert (
        fake_news_announcment("08.11.2022 11:58")
    ) == "До выхода курса осталось: 2 минуты"

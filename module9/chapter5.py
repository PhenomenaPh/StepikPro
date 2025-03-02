from collections.abc import Callable
from datetime import datetime, date


def power(degree: int) -> Callable:
    def _power_in_degree(x: int):
        return x**degree

    return _power_in_degree


def generator_square_polynom(a: float, b: float, c: float) -> Callable:
    def _generate_square_polynom_impl(x: float) -> float:
        return (a * x**2) + (b * x) + c

    return _generate_square_polynom_impl


def sourcetemplate(url: str) -> Callable:
    def sourcetemplate_impl(**kwags) -> str:
        if kwags:
            nonlocal url
            url += "?"
            for k, v in sorted(kwags.items(), key=lambda x: x[0]):
                url += f"{str(k)}={str(v)}&"

            return url.strip("&")
        else:
            return url

    return sourcetemplate_impl


def date_formatter(country_code: str) -> Callable:
    def date_formatter_impl(dt: date) -> str:
        d = {"ru": "%d.%m.%Y", "us": "%m-%d-%Y", "ca": "%Y-%m-%d", "br": "%d/%m/%Y", "fr": "%d.%m.%Y", "pt": "%d-%m-%Y"}
        return dt.strftime(d[country_code])

    return date_formatter_impl

def sort_priority(values: list, group: list | tuple | set) -> None:

    def get_priority(x):
        return 0 if x in group else 1, x

    values[:] = sorted(values, key = get_priority)




if __name__ == "__main__":
    date_ru = date_formatter('ru')
    today = date(2022, 1, 25)
    print(date_ru(today))

from datetime import date
from functools import singledispatch, singledispatchmethod

from dateutil.relativedelta import relativedelta


class Processor:
    @singledispatch
    @staticmethod
    def process(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @process.register
    @staticmethod
    def process_number(data: int | float):
        return data * 2

    @process.register
    @staticmethod
    def process_string(data: str):
        return data.upper()

    @process.register
    @staticmethod
    def process_list(data: list):
        return sorted(data)

    @process.register
    @staticmethod
    def process_tuple(data: tuple):
        return tuple(sorted(data))


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @neg.register
    @staticmethod
    def negate_int(data: int | float):
        return -data

    @neg.register
    @staticmethod
    def negate_str(data: bool):
        return not data


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register
    @staticmethod
    def format_int(data: int):
        print(f"Целое число: {data}")

    @format.register
    @staticmethod
    def format_float(data: float):
        print(f"Вещественное число: {data}")

    @format.register
    @staticmethod
    def format_tuple(data: tuple):
        print(f"Элементы кортежа: {', '.join(map(repr, data))}")

    @format.register
    @staticmethod
    def format_list(data: list):
        print(f"Элементы списка: {', '.join(map(repr, data))}")

    @format.register
    @staticmethod
    def format_dict(data: dict):
        print(f"Пары словаря: {', '.join(f'({repr(k)}, {repr(v)})' for k, v in data.items())}")


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register
    def _from_date(self, birth_date: date):
        self.birth_date = birth_date

    @__init__.register
    def _from_isoformat(self, birth_date: str):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError("Аргумент переданного типа не поддерживается")

    @__init__.register
    def _from_tuple(self, birth_date: tuple | list):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError("Аргумент переданного типа не поддерживается")

    @property
    def age(self):
        """Текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день"""
        return relativedelta(date.today(), self.birth_date).years


if __name__ == "__main__":
    birthday = date(2020, 9, 18)
    today = date.today()
    birthinfo = BirthInfo(birthday)
    true_age = current_age(birthday, today)

    print(birthinfo.age == true_age)

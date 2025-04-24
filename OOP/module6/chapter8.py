from keyword import kwlist
import random


class NonKeyword:
    def __init__(self, name) -> None:
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:  # проверка на то, как осуществляется обращение
            return self
        if self._name not in instance.__dict__:
            raise AttributeError("Атрибут не найден")
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if value in kwlist:
            raise ValueError("Некорректное значение")
        instance.__dict__[self._name] = value


class NonNegativeInteger:
    def __init__(self, name, default=None) -> None:
        self._name = name
        self.default = default

    def __get__(self, instance, owner):
        if instance is None:  # проверка на то, как осуществляется обращение
            return self

        if self._name not in instance.__dict__:
            if self.default is not None:
                return self.default
            else:
                raise AttributeError("Атрибут не найден")
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if isinstance(value, int) and value >= 0:
            instance.__dict__[self._name] = value
        else:
            raise ValueError("Некорректное значение")


class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __set_name__(self, owner, name):
        self._name = name

    def __init__(self, times):
        self.times = times

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._name not in instance.__dict__:
            raise AttributeError("Атрибут не найден")

        if self.times > 0:
            self.times -= 1
            return instance.__dict__[self._name]

        else:
            raise MaxCallsException("Превышено количество доступных обращений")

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


class TypeChecked:
    def __set_name__(self, owner, name):
        self._name = name

    def __init__(self, *args):
        self.input_types = args

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self._name not in instance.__dict__:
            raise AttributeError("Атрибут не найден")
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if isinstance(value, self.input_types):
            instance.__dict__[self._name] = value
        else:
            raise TypeError("Некорректное значение")


class RandomNumber:
    def __set_name__(self, owner, name):
        self._name = name

    def __init__(self, start, end, cache: bool = False):
        self.start = start
        self.end = end
        self.cache = cache

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.cache and self._name in instance.__dict__:
            return instance.__dict__[self._name]

        num = random.randint(self.start, self.end)

        if self.cache:
            instance.__dict__[self._name] = num

        return num

    def __set__(self, instance, value):
        raise AttributeError("Изменение невозможно")


class Versioned:
    def __set_name__(self, owner, name):
        self._name = name
        self._name_history = f"{name}_history"

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self._name not in instance.__dict__:
            raise AttributeError("Атрибут не найден")

        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if self._name not in instance.__dict__:
            instance.__dict__[self._name] = value
            instance.__dict__[self._name_history] = [value]

        else:
            instance.__dict__[self._name_history].append(value)
            instance.__dict__[self._name] = value

    def get_version(self, instance, n):
        return instance.__dict__[self._name_history][n - 1]

    def set_version(self, instance, n, value):
        value = instance.__dict__[self._name_history][n - 1]
        instance.__dict__[self._name] = value


if __name__ == "__main__":

    class Student:
        age = Versioned()

    student = Student()

    student.age = 18
    student.age = 19

    print(student.age)

class Person:
    def __init__(self, name: str, surname: str) -> None:
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname: str):
        name, surname = fullname.split()
        self.name = name
        self.surname = surname


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    hash_final = hash_value % 10**9
    return hash_final


class Account:
    def __init__(self, login: str, password: str) -> None:
        self._login = login
        self.password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        raise AttributeError("Изменение логина невозможно")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = hash_function(password)


class QuadraticPolynomial:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b**2 - 4 * self.a * self.c < 0:
            return None
        return (-self.b - (self.b**2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def x2(self):
        if self.b**2 - 4 * self.a * self.c < 0:
            return None
        return (-self.b + (self.b**2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)

    @property
    def view(self):
        a = f"{self.a}x^2"
        b = f"{['+', '-'][self.b < 0]} {abs(self.b)}x"
        c = f"{['+', '-'][self.c < 0]} {abs(self.c)}"

        return f"{a} {b} {c}"

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, value):
        self.a, self.b, self.c = value


class Color:
    def __init__(self, hexcode: str) -> None:
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return self._hexcode

    @hexcode.setter
    def hexcode(self, value):
        self._hexcode = value

        self.r = int(value[:2], 16)
        self.g = int(value[2:4], 16)
        self.b = int(value[4:], 16)


if __name__ == "__main__":
    color = Color("0000FF")

    print(color.hexcode)
    print(color.r)
    print(color.g)
    print(color.b)

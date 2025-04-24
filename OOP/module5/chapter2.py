from functools import singledispatchmethod


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book({repr(self.title)}, {repr(self.author)}, {self.year})"

    def __str__(self):
        return f"{self.title} ({self.author}, {self.year})"


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __repr__(self):
        return f"Rectangle({self.length}, {self.width})"


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(
        self,
    ):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"Вектор на плоскости с координатами ({self.x}, {self.y})"


class IPAddress:
    @singledispatchmethod
    def __init__(self) -> None:
        raise TypeError("Unsupported type")

    @__init__.register(list)
    @__init__.register(tuple)
    def __init_iter(self, ip):
        self.ip = ".".join(map(str, ip))

    @__init__.register(str)
    def __init_str(self, ip):
        self.ip = ip

    def __str__(self):
        return f"{self.ip}"

    def __repr__(self):
        return f"IPAddress({repr(self.ip)})"


class PhoneNumber:
    def __init__(self, number: str):
        self.number = number.replace(" ", "")

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.number)})"

    def __str__(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"


class AnyClass:
    def __init__(self, **data):
        self.__dict__.update(data)

    def _prepare_text_to_return(self, text_to_return):
        return ", ".join(f"{key}={repr(value)}" for key, value in self.__dict__.items())

    def __repr__(self) -> str:
        text_to_return = self._prepare_text_to_return(self)
        return f"{self.__class__.__name__}({text_to_return})"

    def __str__(self) -> str:
        text_to_return = self._prepare_text_to_return(self)
        return f"{self.__class__.__name__}: {text_to_return}"


if __name__ == "__main__":
    cowboy = AnyClass(name="John", surname="Marston")

    print(str(cowboy))
    print(repr(cowboy))

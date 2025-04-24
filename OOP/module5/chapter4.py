class ReversibleString:
    def __init__(self, string: str) -> None:
        self.string = string

    def __str__(self) -> str:
        return self.string

    def __neg__(self) -> str:
        return ReversibleString(self.string[::-1])


class Money:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.amount} руб."

    def __pos__(self) -> int:
        return self.__class__(abs(self.amount))

    def __neg__(self) -> int:
        return self.__class__(-abs(self.amount))


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __pos__(self) -> int:
        return self.__class__(self.x, self.y)

    def __neg__(self) -> int:
        return self.__class__(-self.x, -self.y)

    def __abs__(self) -> int:
        return (self.x**2 + self.y**2) ** 0.5


class ColoredPoint:
    def __init__(self, x: int, y: int, color: tuple[int, int, int] = (0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.color = color

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"ColoredPoint({self.x}, {self.y}, {self.color})"

    def __pos__(self) -> int:
        return self.__class__(self.x, self.y, self.color)

    def __neg__(self) -> int:
        return self.__class__(-self.x, -self.y, self.color)

    def __invert__(self) -> int:
        return self.__class__(self.y, self.x, tuple(255 - c for c in self.color))


class Matrix:
    def __init__(self, rows: int, cols: int, data: list[list[int]]) -> None:
        self.rows = rows
        self.cols = cols
        self.data = data

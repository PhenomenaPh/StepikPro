class ColoredPoint:
    def __init__(self, x: int, y: int, color: str):
        self._x = x
        self._y = y
        self._color = color

    @property
    def color(self):
        return self._color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def _fields(self):
        return self.x, self.y, self.color

    def __repr__(self):
        return f"ColoredPoint({repr(self.x)}, {repr(self.y)}, {repr(self.color)})"

    def __eq__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return self.x == other.x and self.y == other.y and self.color == other.color

    def __ne__(self, other):
        if not isinstance(other, ColoredPoint):
            return NotImplemented
        return self.x != other.x or self.y != other.y or self.color != other.color

    def __hash__(self):
        return hash(self._fields)


class Row:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __setattr__(self, key, value):
        if key not in self.__dict__:
            raise AttributeError("Установка нового атрибута невозможна")
        else:
            raise AttributeError("Изменение значения атрибута невозможно")

    def __delattr__(self, key):
        raise AttributeError("Удаление атрибута невозможно")

    def __repr__(self):
        values = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"Row({', '.join(values)})"

    def __eq__(self, other):
        if not isinstance(other, Row):
            return NotImplemented
        return list(self.__dict__.items()) == list(other.__dict__.items())

    def __ne__(self, other):
        if not isinstance(other, Row):
            return NotImplemented
        return list(self.__dict__.items()) != list(other.__dict__.items())

    def __hash__(self):
        return hash(tuple(self.__dict__.items()))

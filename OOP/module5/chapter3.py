from functools import total_ordering


@total_ordering
class Word:
    def __init__(self, word: str):
        self.word = word

    def __str__(self):
        return f"{self.word.capitalize()}"

    def __repr__(self):
        return f"Word({repr(self.word)})"

    def __eq__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) == len(other.word)

    def __lt__(self, other):
        if not isinstance(other, Word):
            return NotImplemented
        return len(self.word) < len(other.word)


@total_ordering
class Month:
    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if not isinstance(other, Month | tuple):
            return NotImplemented
        if isinstance(other, tuple):
            return (self.year, self.month) == other

        return self.year == other.year and self.month == other.month

    def __gt__(self, other):
        if not isinstance(other, Month | tuple):
            return NotImplemented
        if isinstance(other, tuple):
            return (self.year, self.month) > other
        return self.year > other.year or (self.year == other.year and self.month > other.month)


@total_ordering
class Version:
    def __init__(self, version: str):
        self.version = version

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, value):
        value_list = list(map(int, value.split(".")))
        len_value = len(value_list)

        if len_value < 3:
            zero_to_add = 3 - len_value
            value_list.extend([0] * zero_to_add)

        self._version = value_list

    def __repr__(self):
        return f"Version({repr('.'.join(map(str, self._version)))})"

    def __str__(self):
        return f"{self._version[0]}.{self._version[1]}.{self._version[2]}"

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._version == other._version

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return self._version < other._version


class Matrix:
    def __init__(self, rows: int, cols: int, value: int = 0):
        self.rows = rows
        self.cols = cols
        self.value = value

        self._matrix = self._create_matrix()

    def _create_matrix(self):
        return [[self.value for _ in range(self.cols)] for _ in range(self.rows)]

    def get_value(self, row: int, col: int):
        value = self._matrix[row][col]
        return value

    def set_value(self, row: int, col: int, value: int):
        self._matrix[row][col] = value

    def __repr__(self) -> str:
        return f"Matrix({self.rows}, {self.cols})"

    def __str__(self) -> str:
        return "\n".join(" ".join(map(str, row)) for row in self._matrix)

    def __pos__(self):
        new_class = self.__class__(self.rows, self.cols, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_class.set_value(row, col, self.get_value(row, col))
        return new_class

    def __neg__(self):
        new_class = self.__class__(self.rows, self.cols, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_class.set_value(row, col, -self.get_value(row, col))
        return new_class

    def __invert__(self):
        new_class = self.__class__(self.cols, self.rows, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_class.set_value(row=col, col=row, value=self.get_value(row=row, col=col))
        return new_class

    def __round__(self, ndigits: int = None):
        new_class = self.__class__(self.rows, self.cols, self.value)
        for row in range(self.rows):
            for col in range(self.cols):
                new_class.set_value(row=row, col=col, value=round(self.get_value(row, col), ndigits=ndigits))
        return new_class


if __name__ == "__main__":
    matrix = Matrix(2, 3, 1)

    plus_matrix = +matrix
    minus_matrix = -matrix
    invert_matrix = ~matrix

    print(plus_matrix.cols, plus_matrix.rows)
    print(minus_matrix.cols, minus_matrix.rows)
    print(invert_matrix.cols, invert_matrix.rows)

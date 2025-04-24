class Rectangle:
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

        self._perimeter = None
        self._area = None

    def get_perimeter(self):
        self._perimeter = 2 * (self.length + self.width)

        return self._perimeter

    def get_area(self):
        self._area = self.length * self.width

        return self._area

    perimeter = property(get_perimeter)
    area = property(get_area)


class HourClock:
    def __init__(self, hours: int):
        self._hours = hours

    def get_hour(self):
        return self._hours

    def set_hour(self, hours: int):
        if hours not in range(1, 13) or not isinstance(hours, int):
            raise ValueError("Некорректное время")
        self._hours = hours

    hours = property(get_hour, set_hour)


if __name__ == "__main__":
    time = HourClock("asdfsdfafsd")
    print(time.hours)

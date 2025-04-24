from math import pi
from typing import Type


class Gun:
    def __init__(self):
        self.n = 0
        pass

    def shoot(self):
        if self.n % 2:
            print("paf")
        else:
            print("pif")
        self.n += 1

    def shots_count(self):
        return self.n

    def shots_reset(self):
        self.n = 0


class House:
    def __init__(self, color, rooms):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color: str):
        self.color = new_color

    def add_rooms(self, n: int):
        self.rooms += n


class Bee:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def move_up(self, n):
        self.y += n

    def move_down(self, n):
        self.y -= n

    def move_right(self, n):
        self.x += n

    def move_left(self, n):
        self.x -= n


class Scales:
    def __init__(self) -> None:
        self.left_scale = 0
        self.right_scale = 0

    def add_right(self, n: int):
        self.right_scale += n

    def add_left(self, n: int):
        self.left_scale += n

    def get_result(self):
        if self.left_scale == self.right_scale:
            return "Весы в равновесии"

        elif self.right_scale > self.left_scale:
            return "Правая чаша тяжелее"

        else:
            return "Левая чаша тяжелее"


class Vector:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def abs(self):
        return abs((self.x**2 + self.y**2) ** (1 / 2))


class Numbers:
    def __init__(self) -> None:
        self.numbers = []

    def add_number(self, n: int):
        self.numbers.append(n)

    def get_even(self):
        return [i for i in self.numbers if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.numbers if i % 2 != 0]


class TextHandler:
    def __init__(self) -> None:
        self.words = []

    def add_words(self, text: str):
        self.words.extend(text.split())

    def get_shortest_words(self):
        min_val = len(min(self.words, key=len, default=""))
        return list(filter(lambda word: len(word) == min_val, self.words))

    def get_longest_words(self):
        max_val = len(max(self.words, key=len, default=""))
        return list(filter(lambda word: len(word) == max_val, self.words))


class Todo:
    def __init__(self) -> None:
        self.things = []

        self.lowest_priority = float("inf")
        self.highest_priority = 0

    def add(self, thing_name: str, thing_priority: int):
        self.things.append((thing_name, thing_priority))

        if thing_priority < self.lowest_priority:
            self.lowest_priority = thing_priority

        if thing_priority > self.highest_priority:
            self.highest_priority = thing_priority

    def get_by_priority(self, priority: int):
        return [i[0] for i in filter(lambda thing: thing[1] == priority, self.things)]

    def get_low_priority(self):
        return [i[0] for i in list(filter(lambda thing: thing[1] == self.lowest_priority, self.things))]

    def get_high_priority(self):
        return [i[0] for i in list(filter(lambda thing: thing[1] == self.highest_priority, self.things))]


class Postman:
    def __init__(self) -> None:
        self.delivery_data = []

    def add_delivery(self, street: str, house_number: int, apartment_number: int):
        delivery_to_collect = (street, house_number, apartment_number)

        if delivery_to_collect not in self.delivery_data:
            self.delivery_data.append(delivery_to_collect)

    def get_houses_for_street(self, street: str):
        houses_list = list(dict.fromkeys(i[1] for i in self.delivery_data if i[0] == street))

        return houses_list

    def get_flats_for_house(self, street: str, house_number: int):
        return [i[2] for i in self.delivery_data if i[1] == house_number and i[0] == street]


class Wordplay:
    def __init__(self, words: list[str] = None) -> None:
        self.words = words.copy() if words else []

    def add_word(self, word: str):
        if word not in self.words:
            self.words.append(word)

    def words_with_length(self, n: int):
        return list(filter(lambda x: len(x) == n, self.words))

    def only(self, *args):
        return [i for i in self.words if set(i).issubset(set(args))]

    def avoid(self, *args):
        return [i for i in self.words if set(i).isdisjoint(set(args))]


class Knight:
    def __init__(self, horizontal: str, vertical: int, color: str) -> None:
        self.chrs = ("a", "b", "c", "d", "e", "f", "g", "h")

        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self) -> str:
        return "N"

    def can_move(self, horizontal: str, vertical: int) -> bool:
        ver_val = abs(vertical - self.vertical)
        hor_val = abs(self.chrs.index(horizontal) - self.chrs.index(self.horizontal))

        return ver_val * hor_val == 2 and ver_val + hor_val == 3

    def move_to(self, horizontal: str, vertical: int) -> None:
        if self.can_move(horizontal=horizontal, vertical=vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        for i in range(8, 0, -1):
            for j in self.chrs:
                if (i, j) == (self.vertical, self.horizontal):
                    print("N", end="", sep="")
                elif self.can_move(j, i):
                    print("*", end="", sep="")
                else:
                    print(".", sep="", end="")
            print()


class Circle:
    def __init__(self, radius) -> None:
        self._radius = radius

        self._diameter = radius * 2
        self._area = pi * radius**2

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area


class BankAccount:
    def __init__(self, balance: int = 0) -> None:
        self._balance = balance
        pass

    def get_balance(self):
        return self._balance

    def deposit(self, amount: int):
        self._balance += amount

    def withdraw(self, amount: int):
        if amount > self._balance:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount

    def transfer(self, account: Type["BankAccount"], amount: int):
        if amount > self._balance:
            raise ValueError("На счете недостаточно средств")
        else:
            self._balance -= amount
            account.deposit(amount)


class User:
    def __init__(self, name: str, age: int) -> None:
        if not (isinstance(name, str) and name.isalpha()):
            raise ValueError("Некорректное имя")

        if not (isinstance(age, int) and age in range(0, 111)):
            raise ValueError("Некорректный возраст")

        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        if not (isinstance(name, str) and name.isalpha()):
            raise ValueError("Некорректное имя")
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        if not (isinstance(age, int) and age in range(0, 111)):
            raise ValueError("Некорректный возраст")
        self._age = age


if __name__ == "__main__":
    invalid_names = (-1, True, '', [], '123456', 'Меган906090')

    for name in invalid_names:
        try:
            user = User(name, 37)
        except ValueError as e:
            print(e)

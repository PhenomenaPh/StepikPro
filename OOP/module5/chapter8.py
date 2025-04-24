class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == "total":
            return object.__getattribute__(self, "price") * object.__getattribute__(self, "quantity")
        elif name == "name":
            return object.__getattribute__(self, "name").title()
        return object.__getattribute__(self, name)


class Logger:
    def __setattr__(self, name, value):
        print(f"Изменение значения атрибута {name} на {value}")
        object.__setattr__(self, name, value)

    def __delattr__(self, name):
        print(f"Удаление атрибута {name}")
        object.__delattr__(self, name)


class Ord:
    def __getattribute__(self, name):
        return ord(str(name))


class DefaultObject:
    def __init__(self, default=None, **kwargs):
        self.default = default

        for k, v in kwargs.items():
            self.__dict__[k] = v

    def __getattr__(self, attr):
        return self.default


class NonNegativeObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __setattr__(self, name, value):
        if isinstance(value, (int, float)):
            value = abs(value)
        object.__setattr__(self, name, value)


class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattribute__(self, name):
        if name == "attrs_num":
            return len(self.__dict__)
        else:
            return object.__getattribute__(self, name)


class Const:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError("Изменение значения атрибута невозможно")
        else:
            object.__setattr__(self, name, value)

    def __delattr__(self, name):
        if name in self.__dict__:
            raise AttributeError("Удаление атрибута невозможно")


class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self, k, v)

    def __getattribute__(self, name: str):
        if name.startswith("_") and not "__dict__":
            raise AttributeError("Доступ к защищенному атрибуту невозможен")

        return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name in self.__dict__ and name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__setattr__(self, name, value)

    def __delattr__(self, name: str):
        if name.startswith("_"):
            raise AttributeError("Доступ к защищенному атрибуту невозможен")
        object.__delattr__(self, name)

from collections.abc import Mapping
from copy import deepcopy


class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError

        if 0 > index >= len(self.sequence):
            raise IndexError

        return self.sequence[-(index + 1)]


class SparseArray:
    def __init__(self, default):
        self.default = default
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data.get(key, self.default)


class CyclicList:
    def __init__(self, iterable):
        self.data = iterable[::]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        good_index = index % len(self.data)
        return self.data[good_index]

    def pop(self, index):
        if index:
            return self.data.pop(index)
        else:
            return self.data.pop()

    def append(self, element):
        self.data.append(element)


class SequenceZip:
    def __init__(self, *sequences):
        self.sequences = list(zip(*deepcopy(sequences)))

    def __len__(self):
        return len(self.sequences)

    def __getitem__(self, index):
        return self.sequences[index]


class OrderedSet:
    def __init__(self, iterable=()):
        self.data = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self.data)

    def add(self, obj):
        self.data[obj] = None

    def discard(self, obj):
        if obj in self.data:
            del self.data[obj]
        else:
            pass

    def __iter__(self):
        return iter(self.data)

    def __eq__(self, other):
        if not isinstance(other, (set, OrderedSet, frozenset)):
            return NotImplemented
        elif isinstance(other, OrderedSet):
            return list(self.data.keys()) == list(other.data.keys())
        return set(self.data.keys()) == other

    def __ne__(self, other):
        if not isinstance(other, (set, OrderedSet, frozenset)):
            return NotImplemented
        elif isinstance(other, OrderedSet):
            return list(self.data.keys()) != list(other.data.keys())
        return set(self.data.keys()) != other


class PermaDict:
    def __init__(self, data: dict = {}):
        self.data = deepcopy(data)

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return iter(self.data.keys())

    def __delitem__(self, key):
        del self.data[key]

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError("Изменение значения по ключу невозможно")
        self.data[key] = value

    def __len__(self):
        return len(self.data)


class HistoryDict:
    def __init__(self, data: dict = {}):
        self.data = {k: {"current": v, "history": [v]} for k, v in data.items()}

    def keys(self):
        return self.data.keys()

    def values(self):
        return [val["current"] for val in self.data.values()]

    def items(self):
        return [(k, v["current"]) for k, v in self.data.items()]

    def history(self, key):
        return self.data[key].get("history", [])

    def all_history(self):
        return {k: v["history"] for k, v in self.data.items()}

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data.keys())

    def __getitem__(self, key):
        return self.data[key]["current"]

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key]["current"] = value
            self.data[key]["history"].append(value)
        else:
            self.data[key] = {"current": value, "history": [value]}

    def __delitem__(self, key):
        del self.data[key]


class MutableString:
    def __init__(self, string: str = ""):
        self.string = string

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"MutableString({self.string!r})"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __add__(self, other):
        if not isinstance(other, MutableString):
            raise TypeError
        return MutableString(self.string + other.string)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return MutableString(self.string[key])
        return MutableString(self.string[key])

    def __setitem__(self, key, value):
        temp_list = list(self.string)

        if isinstance(key, slice):
            temp_list[key] = value
        else:
            temp_list[key] = value

        self.string = "".join(temp_list)

    def __delitem__(self, key):
        temp_list = list(self.string)

        if isinstance(key, slice):
            del temp_list[key]
        else:
            temp_list.pop(key)

        self.string = "".join(temp_list)


class Grouper(Mapping):
    def __init__(self, iterable, key):
        self.groups = {}
        self.key = key

        for element in iterable:
            self.add(element)

    def __len__(self):
        return len(self.groups)

    def add(self, element):
        key = self.key(element)

        if key not in self.groups:
            self.groups[key] = [element]
        else:
            self.groups[key].append(element)

    def group_for(self, obj):
        return self.key(obj)

    def __iter__(self):
        return iter(self.groups.items())

    def __contains__(self, item):
        return item in self.groups

    def __getitem__(self, item):
        return self.groups[item]


if __name__ == "__main__":
    grouper = Grouper(["hi"], key=lambda s: s[0])

    print(grouper.group_for("hello"))
    print(grouper.group_for("bee"))
    print(grouper["h"])
    print("b" in grouper)

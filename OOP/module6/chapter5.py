import sys
from collections import defaultdict
from copy import deepcopy
from time import perf_counter


class SuppressAll:
    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


class Greeter:
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"До встречи, {self.name}!")


class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.obj, "close"):
            self.obj.close()
        else:
            print("Незакрываемый объект")


class ReadableTextFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")

        lines = [line.strip() for line in self.file]

        return lines

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class Reloopable:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
        return [line for line in self.file]

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


class UpperPrint:
    def __init__(self):
        self.original_stdout = sys.stdout.write

    def _upper_func(self, text: str):
        self.original_stdout(text.upper())

    def __enter__(self):
        sys.stdout.write = self._upper_func

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write = self.original_stdout


class Suppress:
    def __init__(self, *args):
        self.exceptions = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True

        return False


class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()

    def write(self, text: str):
        try:
            self.file1.write(text)
            self.file2.write(text)
        except Exception:
            raise ValueError("Файл закрыт или недоступен для записи")

    def close(self):
        self.file1.close()
        self.file2.close()

    def closed(self):
        if self.file1.closed and self.file2.closed:
            return True
        return False

    def writable(self):
        if any([self.file1.closed, self.file2.closed]) or not all([self.file1.writable(), self.file2.writable()]):
            return False
        return True


class Atomic:
    def __init__(self, data: list | set | dict, deep: bool = False):
        self.data = data
        self.deep = deep

    def __enter__(self):
        if not self.deep:
            self._temp = self.data.copy()
        else:
            self._temp = deepcopy(self.data)

        return self._temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.data, list):
                self.data[:] = self._temp
            elif isinstance(self.data, (set, dict)):
                self.data.clear()
                self.data.update(self._temp)
            return True
        return True


class AdvancedTimer:
    def __init__(self):
        self.last_run = self.min = self.max = None
        self.runs = []
        self.start = perf_counter()

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last_run = perf_counter() - self.start
        self.runs.append(self.last_run)

        if not self.min or self.last_run < self.min:
            self.min = self.last_run
        if not self.max or self.last_run > self.max:
            self.max = self.last_run

        return False


class HtmlTag:
    indent = -1

    def __init__(self, tag: str, inline: bool = False):
        self.tag = tag
        self.inline = inline

    def __enter__(self):
        self.__class__.indent += 1

        if not self.inline:
            print(f"{'  ' * self.__class__.indent}<{self.tag}>")
        return self

    def print(self, text: str):
        if self.inline:
            print(f"{'  ' * self.__class__.indent}<{self.tag}>{text}</{self.tag}>")
        else:
            print(f"{'  ' * self.__class__.indent * 2}{text}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self.inline:
            print(f"{'  ' * self.__class__.indent}</{self.tag}>")
        self.__class__.indent -= 1


class TreeBuilder:
    def __init__(self) -> None:
        self.depth = 0
        self.tree = defaultdict(list)

    def structure(self):
        return self.tree[0]

    def __enter__(self):
        self.depth += 1
        return self

    def add(self, obj):
        self.tree[self.depth].append(obj)

    def __exit__(self, *args, **kwargs):
        if self.tree[self.depth]:
            self.tree[self.depth - 1].append(self.tree[self.depth])
            del self.tree[self.depth]
        self.depth -= 1


class TreeBuilderv2:
    def __init__(self) -> None:
        self.knots = [[]]

    def __enter__(self):
        self.knots.append([])

    def add(self, obj):
        self.knots[-1].append(obj)

    def structure(self):
        return self.knots[-1]

    def __exit__(self, *args, **kwargs):
        if self.knots[-1]:
            self.knots[-2].append(self.knots[-1])

        del self.knots[-1]


if __name__ == "__main__":


    pass

import sys
from contextlib import contextmanager


@contextmanager
def make_tag(tag: str):
    print(tag)
    yield
    print(tag)


@contextmanager
def reversed_print():
    current_std_write = sys.stdout.write
    sys.stdout.write = lambda x: current_std_write(x[::-1])
    yield
    sys.stdout.write = current_std_write


@contextmanager
def safe_write(filename: str):
    try:
        current_stdout = sys.stdout
        stdout = open(filename, "a")
        initial_position = stdout.tell()
        yield stdout

    except Exception as e:
        print(f"Во время записи в файл было возбуждено исключение {e.__class__.__name__}")
        stdout.seek(initial_position)  # reset the position to the initial position
        stdout.truncate()  # truncate the file to the initial position
    finally:
        stdout.close()  # close the file
        stdout = current_stdout  # reset the stdout to the original stdout


@contextmanager
def safe_open(filename: str, mode: str = "r"):
    try:
        file = open(filename, mode)
        yield (file, None)
    except Exception as e:
        yield (None, e.__class__.__name__)

    finally:
        if file:
            file.close()

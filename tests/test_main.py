import pytest
from pathlib import Path
from zipfile import ZipFile
import sys
import io


def get_text_fixtures(filepath):
    with ZipFile(filepath, "r") as zf:
        files = [
            (zf.filelist[i], zf.filelist[i + 1])
            for i in range(0, len(zf.filelist) - 1, 2)
        ]
        new_fixt = [
            (zf.read(test_file).decode("utf-8"), zf.read(clue).decode("utf-8"))
            for test_file, clue in files
        ]
    return new_fixt


zip_file = [name for name in Path.cwd().iterdir() if name.suffix == ".zip"][0]
test_fixtures = get_text_fixtures(zip_file)


@pytest.mark.parametrize("test_input,expected", test_fixtures)
def test_exec(test_input, expected):
    # тут подменяем стандартный выход консоли временным, чтобы нормально спарсить ответ
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    exec(
        "from main import *\n" + test_input, globals()
    )  # выполняем код из списка, по сути читаем файл с вопросом и выполняем его.
    result = sys.stdout.getvalue().strip()  # дергаем ответ из стандартного вывода
    sys.stdout = old_stdout  # возвращаем стандартный вывод на место
    assert result == expected  # проверяем результатыo

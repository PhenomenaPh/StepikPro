from pathlib import Path
from zipfile import ZipFile

f_path = Path.cwd() / "desktop.zip"


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f"{size} B"
    elif 1000 <= size < 1000000:
        return f"{round(size / 1024)} KB"
    elif 1000000 <= size < 1000000000:
        return f"{round(size / 1048576)} MB"
    else:
        return f"{round(size / 1073741824)} GB"


with ZipFile(f_path) as z_f:

    for f in z_f.infolist():

        s_len = f.filename.rstrip('/').split('/')
        print(
            '  ' * (len(s_len) - 1),
            s_len[-1],
            '' if f.is_dir() else f' {convert_bytes(f.file_size)}',
            sep=''
         )

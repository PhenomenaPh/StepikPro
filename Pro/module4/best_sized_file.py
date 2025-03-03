from zipfile import ZipFile
from pathlib import Path

with ZipFile(Path.cwd() / 'workbook.zip') as z:
    f_name = ''
    f_value = 0.

    for obj in z.infolist():

        if not obj.is_dir():
            V = 1 - (obj.compress_size / obj.file_size)

            if V > f_value:
                f_name = obj.filename.rsplit('/', maxsplit=1)[-1]
                f_value = V
    print(f_name)



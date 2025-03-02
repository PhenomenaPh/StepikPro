from zipfile import ZipFile
from pathlib import Path


file_path = Path().cwd() / 'workbook.zip'

with ZipFile(file_path) as z:
    file_val = 0
    file_ziped_value = 0

    for obj in z.infolist():

        if not obj.is_dir():
            file_val += obj.file_size
            file_ziped_value += obj.compress_size

    print(f'Объем исходных файлов: {file_val} байт(а)')
    print(f'Объем сжатых файлов: {file_ziped_value} байт(а)')


from zipfile import ZipFile
from pathlib import Path

file_path = Path.cwd() / 'workbook.zip'

with ZipFile(file_path) as z:
    cnt = 0
    for obj in z.infolist():
        if not obj.is_dir():
            cnt += 1
    print(cnt)




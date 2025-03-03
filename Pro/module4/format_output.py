from zipfile import ZipFile
from pathlib import Path
from datetime import datetime

with ZipFile(Path.cwd() / 'workbook.zip') as z:
    sorted_vals = sorted((i for i in z.filelist if not i.is_dir()),
                         key=lambda x: x.filename.split('/')[-1])

    for obj in sorted_vals:
        print(f'{obj.filename.split("/")[-1]}',
              f'  Дата модификации файла: {datetime(*obj.date_time)}',
              f'  Объем исходного файла: {obj.file_size} байт(а)',
              f'  Объем сжатого файла: {obj.compress_size} байт(а)',
              sep='\n'
              )
        print()




from zipfile import ZipFile
from pathlib import Path

with ZipFile(Path.cwd() / 'workbook.zip') as z:
    values = (i for i in z.infolist() if not i.is_dir())
    init_dt = (2021, 11, 30, 14, 22, 0)

    true_dts = sorted([i.filename.rsplit('/')[-1] for i in values if i.date_time >= init_dt])

    print(*true_dts, sep='\n')




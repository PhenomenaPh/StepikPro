import json
from pathlib import Path
from zipfile import ZipFile

names: list[tuple[str, str]] = []
with ZipFile('data.zip') as z:

    for file in z.infolist():
        f_name = Path(file.filename).resolve()

        if f_name.suffix == '.json':

            with z.open(file.filename) as f:
                try:
                    j_file = json.load(f)
                except Exception:
                    pass

                if j_file['team'] == 'Arsenal':
                    names.append((j_file['first_name'], j_file['last_name']))

for name, s_name in sorted(names):
        print(name, s_name)


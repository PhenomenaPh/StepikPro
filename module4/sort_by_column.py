import csv
from pathlib import Path

data_path = Path.cwd().parent / "data" / "deniro.csv"

column_to_sort = int(input()) - 1

with open(data_path, encoding="utf-8") as file:

    rows = csv.reader(file)

    sorted_rows = sorted(
        rows,
        key=lambda x: (
            int(x[column_to_sort]) if x[column_to_sort].isdigit() else x[column_to_sort]
        ),
    )

    for row in sorted_rows:
        print(*row, sep=",")

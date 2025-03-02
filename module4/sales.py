from pathlib import Path as Pt
import csv

data_path = Pt.cwd().parent / "data" / "sales.csv"

with open(data_path, encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter=";", quotechar='"')
    filtered_rows = filter(lambda x: int(x["new_price"]) < int(x["old_price"]), rows)

    for row in filtered_rows:
        print(f"{row['name']}")

import csv
from pathlib import Path


data_path = Path.cwd().parent / "data" / "domain_usage.csv"

with open(data_path, encoding="utf-8") as file:

    domens_count_dict = {}
    rows = csv.DictReader(file)

    for row in rows:

        domen = row["email"].rsplit("@", maxsplit=1)[1]
        domens_count_dict[domen] = domens_count_dict.get(domen, 0) + 1

    sorted_dict = sorted(domens_count_dict.items(), key=lambda x: (x[1], x[0]))

with open("data.csv", "w", encoding="utf-8", newline="") as file:
    colums = ["domain", "count"]
    writer = csv.writer(file)
    writer.writerow(colums)

    for row in sorted_dict:
        writer.writerow(row)

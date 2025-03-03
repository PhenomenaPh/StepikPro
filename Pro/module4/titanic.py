import csv
from pathlib import Path


file_path = Path.cwd().parent / "data" / "titanic.csv"

with open(file_path, encoding="utf-8") as f:
    men_list = []
    women_list = []

    rows = list(csv.DictReader(f, delimiter=";"))

    for row in rows:
        if int(row["survived"]):
            if float(row["age"]) < 18:
                if row["sex"] == "male":
                    men_list.append(row["name"])
                else:
                    women_list.append(row["name"])

for value in men_list + women_list:
    print(value)

import csv
from pathlib import Path

file_path = Path.cwd().parent / "data" / "wifi.csv"

with open(file_path, encoding="utf-8") as file:

    district_dict = {}
    rows = csv.DictReader(file, delimiter=";")

    for row in rows:
        district = row["district"]
        acces_points = int(row["number_of_access_points"])
        district_dict[district] = district_dict.get(district, 0) + acces_points

    for row in sorted(district_dict.items(), key=lambda x: (-int(x[1]), x[0])):
        print(*row, sep=": ")

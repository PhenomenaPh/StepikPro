import csv
from pathlib import Path

path_to_data = Path.cwd().resolve() / "data" / "test.csv"


def condense_csv(filename: str, id_name: str):
    data_dict = {}

    with open(filename, "r") as f, open("condensed.csv", "w") as f2:
        reader = csv.reader(f, delimiter=",")

        for row in reader:

            if row[0] not in data_dict:
                data_dict[row[0]] = {id_name: row[0]}
            data_dict[row[0]][row[1]] = row[2]

        writer = csv.DictWriter(f2, fieldnames=data_dict[row[0]])
        writer.writeheader()
        writer.writerows(data_dict.values())

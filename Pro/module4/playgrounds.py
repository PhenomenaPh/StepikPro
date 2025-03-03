import csv
import json
import pprint
from collections import defaultdict
from pathlib import Path

data_dict = defaultdict(lambda: defaultdict(list))
path_to_file = Path.cwd()

with open(path_to_file / "data" / "playgrounds.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")

    for row in reader:
        data_dict[row["AdmArea"]][row["District"]].append(row["Address"])

pprint.pprint(data_dict)
json.dump(data_dict, open("addresses.json", "w", encoding="utf-8"))

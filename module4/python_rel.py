import json
from collections import defaultdict
from pathlib import Path

path_to_file = Path.cwd() / "data" / "countries.json"

json_data = json.load(path_to_file.open())

data_dict = defaultdict(list)

for data in json_data:
    data_dict[data["religion"]].append(data["country"])

json.dump(data_dict, open("religions.json", "w"))

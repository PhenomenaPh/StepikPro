import json
from functools import reduce
from pathlib import Path

path_to_file = Path(__file__).parent.parent / "data" / "people.json"


final_list = []
with open(path_to_file, "r") as f, open("updated_people.json", "w") as f_out:
    jsoned_data = json.load(f)

    keys = set()
    for data in jsoned_data:
        keys |= set(data.keys())

    for data in jsoned_data:
        data |= data.fromkeys(keys - set(data.keys()))

    print(jsoned_data)

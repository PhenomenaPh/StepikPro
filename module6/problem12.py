import json
from collections import ChainMap

with open("zoo.json", "r", encoding="utf-8") as file:
    dicts = ChainMap(json.load(file))

    # Calculate sum of all animals

    print(sum(dicts.values()))

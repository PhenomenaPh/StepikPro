import json


values = json.load(open(0))

for key, value in values.items():
    if isinstance(value, list):
        print(f"{key}: {', '.join(map(str, value))}")
    else:
        print(f"{key}: {value}")

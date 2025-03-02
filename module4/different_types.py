import json
from pathlib import Path

path_to_file = Path(__file__).parent.parent / "data" / "data.json"

with open(path_to_file, "r", encoding="utf-8") as f, open("updated_data.json", "w") as f2:
    oper_funcs = {
        str: lambda x: x + "!",
        int: lambda x: x + 1,
        bool: lambda x: not x,
        list: lambda x: x * 2,
        dict: lambda x: x | {"newkey": None},
    }

    jsoned_value = json.load(f)
    formated_values = [oper_funcs.get(type(i), None)(i) for i in jsoned_value]

    json.dump(formated_values, f2)

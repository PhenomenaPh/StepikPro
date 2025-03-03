import json
from datetime import datetime, time

data_dict = {}
with open("pools.json", "r", encoding="utf-8") as f:
    jsoned_data = json.load(f)

    for pool in jsoned_data:
        time_range = pool["WorkingHoursSummer"]["Понедельник"]
        start_time, end_time = map(lambda x: datetime.strptime(x, "%H:%M").hour, time_range.split("-"))

        if start_time <= 10 and end_time >= 12:
            length, width = pool["DimensionsSummer"]["Length"], pool["DimensionsSummer"]["Width"]
            max_length, max_width = data_dict.get("length", 0), data_dict.get("width", 0)

            if length > max_length or (length == max_length and width > max_width):
                data_dict.update({"length": length, "width": width, "Address": pool["Address"]})

print(f"{data_dict['length']}x{data_dict['width']}", data_dict["Address"], sep="\n")

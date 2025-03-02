import json

with open("data1.json") as f, open("data2.json") as g, open("data_merge.json", "w") as f_out:
    data1 = json.load(f)
    data2 = json.load(g)

    new_json = data1 | data2

    json.dump(new_json, f_out)

import csv

results_dict = {}
with open("../exam_results.csv", "r", encoding="utf-8") as f:
    writer = csv.DictReader(f)

    for row in writer:
        full_name = f"{row['name']}"
        print(row)

import csv
import json
from pathlib import Path

path_to_file = Path.cwd() / "module4" / "students.json"

# Use 'with' statement to open the JSON file
with path_to_file.open(encoding="utf-8", mode="r") as json_file:
    data = json.load(json_file)

# Use 'with' statement to open the CSV file
with open("students.csv", "w", encoding="utf-8", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["name", "phone"], delimiter=",")
    writer.writeheader()

    final_list = []
    for student in data:
        if student["age"] >= 18 and student["progress"] >= 75:
            final_list.append({"name": student["name"], "phone": student["phone"]})

    writer.writerows(sorted(final_list, key=lambda x: x["name"]))

print("123")

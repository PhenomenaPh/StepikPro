import csv
from pathlib import Path

path_to_file = Path().cwd().parent / "data" / "students_count.csv"

with open(path_to_file, encoding="utf-8") as f, open(
    "sorted_student_counts.csv", "w"
) as f_out:

    reader = csv.DictReader(f)
    columns = reader.fieldnames

    sorted_columns = sorted(
        columns[1:],
        key=lambda x: (int(x.split("-")[0]), x.split("-")[1]),
    )
    writer = csv.DictWriter(f_out, fieldnames=["year"] + sorted_columns)
    writer.writeheader()

    for row in reader:
        writer.writerow(row)

import csv
from pathlib import Path

salary_path = Path.cwd().parent / "data" / "salary_data.csv"

with open(salary_path, encoding="utf-8") as file:
    rows = csv.DictReader(file, delimiter=";")

    mean_salary_dict = {}

    for row in rows:
        company = row["company_name"]
        salary = int(row["salary"])

        if company not in mean_salary_dict:
            mean_salary_dict[company] = {"total": 0, "count": 0}

        mean_salary_dict[company]["total"] += salary
        mean_salary_dict[company]["count"] += 1

    for row in sorted(
        mean_salary_dict.items(),
        key=lambda x: x[1]["total"] / x[1]["count"],
    ):
        print(row[0])

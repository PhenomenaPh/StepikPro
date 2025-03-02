import csv
from datetime import datetime
from pathlib import Path

file_path = Path.cwd().parent / "data" / "name_log.csv"
pattern = "%d/%m/%Y %H:%M"

with open(file_path, encoding="utf-8") as f_in, open(
    "new_name_log.csv", "w", encoding="utf-8", newline=""
) as f_out:

    users_dict = {}
    rows = csv.DictReader(f_in)

    for row in rows:
        mail = row["email"]
        name = row["username"]
        dtime = datetime.strptime(row["dtime"], pattern)

        if mail not in users_dict:
            users_dict[mail] = [name, mail, dtime.strftime(pattern)]

        elif datetime.strptime(users_dict.get(mail)[-1], pattern) < dtime:
            users_dict[mail] = [name, mail, dtime.strftime(pattern)]

    writer = csv.writer(f_out)
    writer.writerow(["username", "email", "dtime"])

    for name, attr in sorted(users_dict.items(), key=lambda x: x[0]):
        writer.writerow(attr)

import csv
from collections import Counter

with open("./name_log.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    # Collecting emails
    emails = Counter(i["email"] for i in reader)

    for email, cnt in sorted(emails.items(), key=lambda x: x[0]):
        print(f"{email}: {cnt}")

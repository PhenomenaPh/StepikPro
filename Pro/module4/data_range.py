from sys import stdin
from datetime import datetime


dates = [datetime.strptime(date.strip(), "%Y-%m-%d") for date in stdin]

min_dt, max_dt = min(dates), max(dates)

print((max_dt - min_dt).days)

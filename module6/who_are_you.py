import csv
from collections import namedtuple
from datetime import datetime

date_pattern, time_pattern = "%d.%m.%Y", "%H:%M"

Friend = namedtuple("Friend", ["surname", "name", "meeting_date", "meeting_time"])

with open('./meetings.csv', 'r') as f:
    rows = csv.reader(f)
    next(rows)

    sorted_data = sorted(map(Friend._make, rows), 
                         key=lambda x: (datetime.strptime(x.meeting_date, date_pattern), 
                                        datetime.strptime(x.meeting_time, time_pattern))
                         )

    for i in sorted_data:
        print(i.surname, i.name)

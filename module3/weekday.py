import calendar
from datetime import datetime

dt_obj = datetime.strptime(input(), "%Y-%m-%d").weekday()

print(calendar.day_name[dt_obj])

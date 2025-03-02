import calendar
from datetime import datetime

dt = datetime.strptime(input(), "%Y %m")

print(calendar.monthrange(dt.year, dt.month)[1])

from datetime import datetime
import calendar

dt = datetime.strptime(input(), "%Y %B")

print(calendar.monthrange(dt.year, dt.month)[1])

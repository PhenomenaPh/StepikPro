import calendar
from datetime import datetime

dt_obj = datetime.strptime(input(), "%Y %b")

calendar.prmonth(dt_obj.year, dt_obj.month)

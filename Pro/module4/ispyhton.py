from datetime import datetime

dates = [datetime.strptime(date_obj, "%d.%m.%Y") for date_obj in open(0)]

if all(dates[i] < dates[i + 1] for i in range(len(dates) - 1)):
    print("ASC")
elif all(dates[i] > dates[i + 1] for i in range(len(dates) - 1)):
    print("DESC")
else:
    print("MIX")

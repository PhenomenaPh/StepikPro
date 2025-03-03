from datetime import datetime, timedelta


def employees_age():
    pattern = "%d.%m.%Y"
    emp_dict = {}

    for _ in range(int(input())):
        name, bd = input().rsplit(maxsplit=1)
        emp_dict.setdefault(datetime.strptime(bd, pattern), []).append(name)

    min_age = min(emp_dict)

    if (s := len(emp_dict[min_age])) > 1:
        print(min_age.strftime(pattern), s)
    else:
        print(min_age.strftime(pattern), "".join(emp_dict[min_age]))


employees_age()

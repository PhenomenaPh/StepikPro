from datetime import datetime


def employees2():

    pattern = "%d.%m.%Y"
    emp_dict = {}

    for _ in range(int(input())):
        name, bd = input().rsplit(maxsplit=1)
        emp_dict.setdefault(datetime.strptime(bd, pattern), []).append(name)

    max_len_age = len(emp_dict[max(emp_dict, key=lambda x: len(emp_dict[x]))])

    best_dates = [
        key.strftime("%d.%m.%Y")
        for key in sorted(emp_dict)
        if len(emp_dict[key]) == max_len_age
    ]

    return best_dates


print(*employees2(), sep="\n")

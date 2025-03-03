from datetime import datetime, timedelta


def employees3():
    pattern = "%d.%m.%Y"
    target_dt = datetime.strptime(input(), pattern)

    good_employes = {}
    for _ in range(int(input())):
        name, bd = input().rsplit(maxsplit=1)
        bd = datetime.strptime(bd, pattern).replace(year=target_dt.year)

        if target_dt < bd <= target_dt + timedelta(days=7):
            good_employes[name] = bd

    if good_employes:
        return min(good_employes, key=good_employes.get)
    else:
        return "Дни рождения не планируются"


print(employees3())

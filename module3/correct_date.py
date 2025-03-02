from is_correct import is_correct

correct_value = 0
while (date_val := input()) != "end":
    day, month, year = map(int, date_val.split("."))

    # date in format DD.MM.YYYY
    if is_correct(day, month, year):
        print("Корректная")
        correct_value += 1
    else:
        print("Некорректная")

print(correct_value)

def get_weekday(number: str):
    week = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье",
    }

    if not isinstance(number, int):
        raise TypeError("Аргумент не является целым числом")
    elif number not in week:
        raise ValueError("Аргумент не принадлежит требуемому диапазону")
    else:
        return week[number]

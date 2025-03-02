import json
from json.decoder import JSONDecodeError

json_name = input()
try:
    with open(json_name, "r") as file:
        try:
            json_data = json.load(file)
            print(json_data)
        except JSONDecodeError:
            print("Ошибка при десириализации")

except FileNotFoundError:
    print('Файл не найден')
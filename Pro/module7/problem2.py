text_name = input()

try:
    with open(text_name, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден")

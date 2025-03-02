values = [int(x.strip()) for x in open(0)]

d = values[1] - values[0]
r = values[1] // values[0]

if all(values[i] - values[i - 1] == d for i in range(2, len(values))):
    print("Арифметическая прогрессия")
elif all(values[i] // values[i - 1] == r for i in range(2, len(values))):
    print("Геометрическая прогрессия")
else:
    print("Не прогрессия")

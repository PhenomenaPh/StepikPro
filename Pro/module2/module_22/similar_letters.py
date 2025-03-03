from sys import stdin

letters = list(map(ord, stdin.read().splitlines()))
print(letters)

if max(letters) <= 121:
    print("en")
elif min(letters) >= 1040:
    print("ru")
else:
    print("mix")

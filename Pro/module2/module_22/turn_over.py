n, x, y, a, b = list(map(int, input().split()))

values = [str(i) for i in range(1, n + 1)]
print(values)


values[x - 1 : y] = reversed(values[x - 1 : y])
values[a - 1 : b] = reversed(values[a - 1 : b])

print(" ".join(values))

# Variant 1 with lists
moves = [int(move.strip()) for move in open(0)]
print("Дима" if len(moves) % 2 == moves[-1] % 2 else "Анри")

# Variant 2 with for loop. Memory efficient
pl1, pl2 = "Анри", "Дима"
move = None

for move in open(0):
    pl1, pl2 = pl2, pl1

print(pl1 if int(move) % 2 != 0 else pl2)

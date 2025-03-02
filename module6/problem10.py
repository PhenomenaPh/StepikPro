import csv
import json
from collections import Counter

counter = Counter()

for i in range(1, 5):
    with open(f"quarter{i}.csv", "r") as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)

        for row in reader:
            product, quantity = row
            counter[product] += int(quantity)

with open("prices.json", "r") as f:
    prices = json.load(f)

# Multiply the quantity of each product by its price and use total method
total = sum(prices[product] * quantity for product, quantity in counter.items())
print(total)

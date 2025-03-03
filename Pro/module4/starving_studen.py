import csv
from pathlib import Path

path_to_file = Path.cwd().parent.resolve() / "data" / "prices.csv"

with open(path_to_file, "r", encoding="utf-8") as file:

    rows = csv.DictReader(file, delimiter=";")
    goods_list = []

    for row in rows:
        shop = row.pop("Магазин")
        good, price = min(row.items(), key=lambda x: int(x[1]))

        goods_list.append((int(price), good, shop))

    best_product = min(goods_list)
    print(f"{best_product[1]}: {best_product[-1]}")

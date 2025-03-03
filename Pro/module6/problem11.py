from collections import Counter

books_cnt = Counter(input().split())
sum_money = 0

for _ in range(int(input())):
    book, price = input().split()

    if books_cnt[book] > 0:
        books_cnt.subtract([book])
        sum_money += int(price)

print(sum_money)

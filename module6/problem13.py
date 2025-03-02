from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

dicts = ChainMap(bread, meat, sauce, vegetables, toppings)

ingridients = Counter(input().split(','))

max_len_product, total_sum, max_len = max(map(len, ingridients.keys())), 0, 0

# Price of the sandwich
for product, cnt in sorted(ingridients.items(), key=lambda x: x[0]):

    total_sum += dicts[product] * cnt
    resulting_string = f'{product:<{max_len_product}} x {cnt}'

    if len(resulting_string) > max_len:
        max_len = len(resulting_string)

    print(resulting_string)

closing_string = f'ИТОГ: {total_sum}р'
max_len = max(max_len, len(closing_string))

print('-' * max_len)
print(closing_string)



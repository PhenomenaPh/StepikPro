from collections import Counter

data = Counter("aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi")

data.__dict__["min_values"] = lambda: [i for i in data.items() if i[1] == min(data.values())]
data.__dict__["max_values"] = lambda: [i for i in data.items() if i[1] == max(data.values())]

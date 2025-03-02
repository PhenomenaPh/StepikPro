from collections import Counter
from operator import itemgetter


def print_bar_chart(data: list | str, mark: str) -> None:
    counter = Counter(data)
    max_val_len = max(map(len, data))

    for i in sorted(counter.items(), key=itemgetter(1), reverse=True):
        print(f"{i[0]:<{max_val_len}} |{mark * i[1]}")

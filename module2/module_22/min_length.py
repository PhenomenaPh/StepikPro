from sys import stdin

value = list(map(int, stdin.read().split()))


def min_length(lengths):
    best_road = min(
        [
            (lengths[0] + lengths[1]) * 2,
            (lengths[0] + lengths[3]) * 2,
            (lengths[1] + lengths[3]) * 2,
            sum(lengths),
        ]
    )
    print(best_road)


min_length(value)

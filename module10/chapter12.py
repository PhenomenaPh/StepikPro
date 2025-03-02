import string
from string import ascii_uppercase
from typing import Iterable
from itertools import combinations, permutations, combinations_with_replacement, chain, product


def words_permutations(word: Iterable[str]):
    permutated_words = sorted(set(permutations(word)))

    for word in permutated_words:
        print(''.join(word))


if __name__ == '__main__':
    print(1)

from functools import lru_cache

@lru_cache()
def sort_word(word: str) -> str:
    return "".join(sorted(word))

@lru_cache()
def ways(n: int):
    if n <= 3:
        return 1
    elif n == 4:
        return 2
    else:
        return ways(n - 1) + ways(n - 3) + ways(n - 4)

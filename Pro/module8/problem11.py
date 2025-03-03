def get_pow(a: int, n: int):
    if n == 0:
        return 1
    else:
        return a * get_pow(a, n - 1)


def get_fast_pow(a: int, n: int):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return get_fast_pow(a * a, n // 2)
    else:
        return a * get_fast_pow(a, n - 1)


def recursive_sum(a: int, b: int):
    if b == 0:
        return a
    else:
        return 1 + recursive_sum(a, b - 1)


def is_power(number: int | float):
    if number == 1:
        return True
    elif number % 2 != 0:
        return False
    else:
        return is_power(number / 2)


def tribonacci(n: int):
    cache = {1: 1, 2: 1, 3: 1}

    def tri_rec(num: int):
        result = cache.get(num)
        if not result:
            result = tri_rec(num - 3) + tri_rec(num - 2) + tri_rec(num - 1)
            cache[num] = result

        return result

    return tri_rec(n)


def is_palindrome(word: str):
    if len(word) < 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])


def to_binary(num: int):
    if num <= 1:
        return str(num)
    return to_binary(num // 2) + str(num % 2)


def recursive_sum_five(n: int):
    if n > 0:
        print(n)
        recursive_sum_five(n - 5)
    print(n)


recursive_sum_five(int(input()))

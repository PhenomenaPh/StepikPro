def fib(n):
    cache = {1: 1, 2: 1}

    def fib_rec(n):
        result = cache.get(n)
        if result is None:
            result = fib_rec(n - 2) + fib_rec(n - 1)
            cache[n] = result
        return result

    return fib_rec(n)


print(fib(6))

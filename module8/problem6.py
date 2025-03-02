def print_digits(n: int):
    if n < 10:
        print(n)
        return
    else:
        print(n % 10)
        print_digits(n // 10)


print_digits(1234)

def recursion_sum(num: int):
    if num // 10 == 0:
        return num
    else:
        last_digit = num % 10
        return last_digit + recursion_sum(num // 10)


print(recursion_sum(int(input())))

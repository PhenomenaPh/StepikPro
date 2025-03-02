def recursion():
    digit = int(input())
    if digit != 0:
        recursion()
    print(digit)


recursion()

def triangle(h: int):
    if h == 0:
        return
    else:
        triangle(h - 1)
        print("*" * h)


triangle(5)

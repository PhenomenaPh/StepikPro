def print_given(*args, **kwargs):

    for i in args:
        print(i, type(i))

    for key, value in sorted(kwargs.items()):
        print(key, value, type(value))

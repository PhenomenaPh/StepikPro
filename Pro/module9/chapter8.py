from functools import wraps


def prefix(string: str, to_the_end: bool = False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a: str = func(*args, **kwargs)

            if to_the_end:
                return a + string
            else:
                return string + a

        return wrapper

    return decorator


def make_html(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            a = func(*args, **kwargs)
            return f"<{tag}>{a}<{tag}>"

        return wraps

    return decorator


def repeat(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                a = func(*args, **kwargs)

            return a

        return wrapper

    return decorator


def strip_range(start: int, end: int, char: str = "."):
    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            func_res: str = func(*args, **kwargs)

            func_mod = func_res[: start + 1] + char * (end - start) % len(func_res) + func_res[end + 1 :]
            return func_mod

        return wrapper

    return decorator


def returns(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            a = func(*args, **kwargs)
            if not isinstance(a, datatype):
                raise TypeError
            else:
                return a

        return wrapper

    return decorator


def takes(*args):
    def decorator(func):
        @wraps(func)
        def wrapper(*inner_args, **kwargs):
            if any(not isinstance(i, args) for i in [*inner_args, *kwargs]):
                raise TypeError
            return func(*inner_args, **kwargs)

        return wrapper

    return decorator


def add_attrs(**take_kwargs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        for k, v in take_kwargs:
            setattr(wrapper, k, v)

        return wrapper

    return decorator


def ignore_exception(*take_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except take_args as e:
                print(f"Исключение {e} обработано")

        return wrapper

    return decorator


class MaxRetriesException(Exception): ...


def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            for i in range(times + 1):
                try:
                    func(*args, **kwargs)
                    break
                except Exception:
                    if i == times:
                        raise MaxRetriesException
        return wrapper

    return decorator

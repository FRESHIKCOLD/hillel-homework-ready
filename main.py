from functools import wraps
from math import isfinite


def shout(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs).upper()
    return wrapper


def positive_only(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        for value in args:
            if type(value) not in (int, float) or value <= 0:
                raise ValueError("Усі позиційні аргументи мають бути додатними числами")
            if isinstance(value, float) and not isfinite(value):
                raise ValueError("Аргументи мають бути скінченними")
        return function(*args, **kwargs)
    return wrapper


@positive_only
def add_two(x):
    return x + 2


@shout
def add_suffix(value):
    return value + "suffix"


if __name__ == "__main__":
    print(add_two(3))
    print(add_suffix("i"))

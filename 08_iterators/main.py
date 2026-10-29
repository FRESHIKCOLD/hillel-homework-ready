from functools import wraps


def log_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("args:", args, "kwargs:", kwargs)
        return function(*args, **kwargs)
    return wrapper


def repeat(times):
    if type(times) is not int or times < 0:
        raise ValueError("times має бути невід'ємним цілим числом")
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator


@log_args
def add(*numbers):
    return sum(numbers)


@repeat(3)
def greet():
    print("Привіт!")


def countdown(n):
    for number in range(n, 0, -1):
        yield number
    yield "Старт!"


if __name__ == "__main__":
    print(add(1, 2, 3))
    greet()
    words = ["кіт", "Python", "гра", "програмування", "мова"]
    for word in words:
        if (length := len(word)) > 4:
            print(word, length)
    for item in countdown(3):
        print(item)

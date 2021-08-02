import math


def decorated_print(func):
    def wrapper(a, b):
        result = func(a, b)
        return print(f"При катетах {a}, {b} гіпотенуза дорівнює {result}")

    return wrapper


@decorated_print
def hipotenuse(a, b):
    result = math.sqrt(a**2 + b**2)
    return int(result)


hipotenuse(3, 4)

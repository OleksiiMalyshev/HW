import math


class WrongType(Exception):
    pass


class WrongResult(Exception):
    pass


class TypeChecker:
    def __init__(self, arg_1, arg_2, waited_result):
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.waited_result = waited_result

    def __call__(self, func):
        def wrap(a, b):
            try:
                if isinstance(a, self.arg_1) and isinstance(b, self.arg_2):
                    result = func(a, b)
                    if isinstance(result, self.waited_result):
                        return result
                    else:
                        raise WrongResult
                else:
                    raise WrongType
            except WrongResult:
                print("Your function returns unexpected type of result")
            except WrongType:
                print("You use func with forbidden types of args")

        return wrap


@TypeChecker(int, int, float)
def hypotenuse(a, b):
    hyp = math.sqrt(a ** 2 + b ** 2)
    return hyp


x, y = 3, 4
print(f'Гіпотенуза - при катетах {x} та {y} -- {hypotenuse(x, y)}')

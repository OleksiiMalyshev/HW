import math


class WrongType(Exception):
    pass


class WrongResult(Exception):
    pass


def type_checker(arg_1, arg_2, waited_result):
    def big_wrap(func):
        def wrap(a, b):
            try:
                if isinstance(a, arg_1) and isinstance(b, arg_2):
                    result = func(a, b)
                    if isinstance(result, waited_result):
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

    return big_wrap


@type_checker(int, int, float)
def hypotenuse(a, b):
    hyp = math.sqrt(a ** 2 + b ** 2)
    return hyp




def decor(func):
    def wrap(*args):
        result = func(*args)
        str_list = [str(el) for el in result]
        return str_list

    return wrap


@decor
def num_to_list(n):
    return [i for i in range(n + 1)]


print(num_to_list(10))

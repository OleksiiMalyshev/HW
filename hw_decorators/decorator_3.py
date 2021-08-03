lst = input("input your list ").split()


def filter(func):
    def wrap(_lst):
        new_list = []
        for i in range(len(_lst)):
            try:
                new_list.append(int(_lst[i]))
            except ValueError:
                continue
        result = func(new_list)
        return result

    return wrap


@filter
def list_sum(_list):
    return sum(_list)


print(list_sum(lst))

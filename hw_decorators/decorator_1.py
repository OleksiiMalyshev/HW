import time


def time_decorator(func):
    def wraper(*args, **kwargs):
        timepoint = time.time()
        result = func(*args, **kwargs)
        print("Time used for this func is -", time.time() - timepoint)
        return result

    return wraper


@time_decorator
def data_input():
    lst = []
    while True:
        data = input("Input your data\nType exit to end - ")
        if data == 'exit':
            break
        lst.append(data)
    print(lst)


data_input()

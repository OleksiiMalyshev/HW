#def my_funk(x):
    #print(type(x))
    #print(id(x))

# int_a = 55
# str_b = 'cursor'
# set_c = {1, 2, 3}
# lst_d = [1, 2, 3]
# dict_e = {'a': 1, 'b': 2, 'c': 3}
#
# print(isinstance(int_a, int))
# print(isinstance(str_b, str))
# print(isinstance(set_c, set))
# print(isinstance(lst_d, list))
# print(isinstance(dict_e, dict))
# lst_d.append(set_c)

# my_funk(int_a)
# my_funk(str_b)
# my_funk(set_c)
# my_funk(lst_d)
# my_funk(dict_e)
# a , b = 10, 20
# apples = "ten"
# peaches = "twenty"
# num_dict = {'apl': apples, 'pch': peaches}
# print("Anna has %(apl)s apples and %(pch)s peaches" % num_dict)

# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# lst_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
# print(lst_comp)
# lst_com = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
# print(lst_com)
#
# lst = []
# for num in range(10):
#     if num % 2 == 0:
#         lst.append(num // 2)
#     else:
#         lst.append(num * 10)
# print(lst)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# dic_cmp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
# print(dic_cmp)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# dic_cmp = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1,11)}
# print(dic_cmp)

# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
# print(dict_comprehension)
#
# d = {}
# for x in range(10):
#     if x ** 3 % 4 == 0:
#         d[x] = x ** 3
# print(d)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
# print(dict_comprehension)
#
# d = {}
# for x in range(10):
#     if x ** 3 % 4 == 0:
#         d[x] = x ** 3
#     else:
#         d[x] = x
# print(d)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
# print(foo(5, 6))
#
# a = lambda x, y : x if x < y  else y
# print(a(5, 6))
# def funk(x, y, z):
#     if y < x and x > z:
#         return z
#     else:
#         return y
# print(funk(1, 2, 3))
#
# foo = lambda x, y, z: z if y < x and x > z else y
# print(foo(1, 2, 3))

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# #print(sorted(lst_to_sort))
# #print(sorted(lst_to_sort, reverse=True))
# new_lst = list(map(lambda x: x * 2,lst_to_sort))
# print(lst_to_sort)
# print(new_lst)

# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
# list_A = list(map(lambda x: x+3, list_A))
# print(list_A)

# import functools

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
# # a = lambda x, y: x + y
# # print(functools.reduce(a, lst_to_sort))
# new_lst = list(filter(lambda elem: (elem % 2 == 1),lst_to_sort))
# print(new_l
# b = [int(i) for i in range(-10,10)]
# lst = list(filter(lambda elem: (elem < 0), b))
# print(lst)
#
# list_1 = [1, 2, 3, 5, 7, 9]
# list_2 = [2, 3, 5, 6, 7, 8]
# lst = list(filter(lambda elem : (elem == elem in list_1), list_2))
# print(lst)

# def add_x_and_y(x, y):
#     """
#     <我是註解>
#     :param x:輸入x
#     :param y:輸入y
#     :return:
#     """
#     sum_num = x + y
#     print(sum_num)
#     return sum_num

#
# a = 10
# b = 4
# add_x_and_y(a, b)


# def add_x_and_multi_y(x, *y):
#     """
#     add x and multi y
#     :param x: 8
#     :param y: (6, 7, 8)
#     :return:
#     """
#     sum_numm = x + sum(y)
#     print(y)
#     return sum_numm

# z = 7
# x = 6
# c = 9
# v = 44
# b = 65
# sum1 = add_x_and_multi_y(z, x, c, v, b)
# print(sum1)

#
# def add_v_and_u_return_multi_value(v, u):
#     sum_nummm = v + u
#     avg = sum_nummm / 2
#
#     return sum_nummm, avg
#
#
# f = 4
# g = 20
# sum3 = add_v_and_u_return_multi_value(f, g)
# print(sum3)
#
# def compare(x, y):
#     return x > y
#
#
# x = 5
# y = 7
# ss = compare(x, y)
# print(ss)

ls = [0, 1, 1, 2, 3, 5, 6, 8, 13, 21, 34, 55]


def is_odd(x):
    return x % 2 == 1


result = list(filter(is_odd, ls))
print(result)

result1 = list(filter(lambda x: x % 2 == 1, ls))  # 可以把上面is_odd那一整串改寫成這一行
print(result1)

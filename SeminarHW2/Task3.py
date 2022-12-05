# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd

my_list = [rnd(-10, 10) for i in range(10)]

print(my_list)

# method 1
# j = len(my_list)
#
# for i in range(j):
#     k = rnd(0, j - 1)
#     elem = my_list.pop(k)
#     my_list.append(elem)

# print(my_list)

# method 2
for i in range(len(my_list)-1, 0, -1):
    j = rnd(0, i + 1)
    my_list[i], my_list[j] = my_list[j], my_list[i]

print(my_list)
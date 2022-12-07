# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint as rnd

my_list = list(rnd(0, 10) for _ in range(rnd(4, 10)))

print(f'{my_list} -> Оригинальный список\n')

mid_index = len(my_list) // 2

list1 = my_list[:mid_index]
list2 = my_list[mid_index:]
list2.reverse()

res_list = list(i * j for i, j in zip(list1, list2))

if len(list1) != len(list2):
    mid_num = list2[-1] * list2[-1]
    res_list.append(mid_num)

print(f'{list1} \n')
print(f'{list2} \n')
print(f'{res_list} -> Результирующий список')
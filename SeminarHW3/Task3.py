# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import randint as rnd

import numpy as numpy

my_list = [round(numpy.random.uniform(0, 100), rnd(1, 4)) for _ in range(11)]
my_list.insert(rnd(0, len(my_list)), rnd(100, 10000))

print(f'{my_list} -> Оригинальный список\n')

floor_list = [round(i % 1, 4) for i in my_list if i % 1 != 0]

print(f'{max(floor_list) - min(floor_list)} -> разница между максимальным и минимальным значением дробной части')
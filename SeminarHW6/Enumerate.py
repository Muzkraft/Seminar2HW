# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с нечетными индексами.
from random import randint as rnd

my_list = list(rnd(0, 10) for _ in range(10))

summa = 0

for i, number in enumerate(my_list):
    if i % 2 != 0:
        summa += number

print(f'{my_list} -> {summa}')
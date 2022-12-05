# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль

from random import randint as rnd

orig_list = list(rnd(1000, 9999) for i in range(10))

print(f' Оригинальный список: \n {orig_list}')

number_del = input('Введите ненавистную вам цифру: ')

my_list = []

for number in orig_list:
    lst = "".join(j for j in str(number) if j != number_del)
    my_list.append(int(lst))

print(f' \n Список без ненацифры: \n {my_list}')

for i, number in enumerate(my_list):
    while len(str(number)) > 1:
        summa = 0
        for digit in str(number):
            if digit.isdigit():
                summa += int(digit)
                number = str(summa)
    else:
        my_list.pop(i)
        my_list.insert(i, int(number))

print(f' \n Приведенные значения: \n {my_list}')

#my_list = list(set(my_list))
#print(my_list)

end_list = [i for n, i in enumerate(my_list) if i not in my_list[:n]]

print(f'\n Финальный список: \n {end_list}')


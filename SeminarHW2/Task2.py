# Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.
from functools import reduce

n = int(input('Введите n: '))

my_list = []
# summa = 0

for i in range(1, n + 1):
    my_list.append(round((1 + 1/i) ** i, 2))

summa = reduce((lambda x, y: x + y), my_list)

# for i in range(len(my_list)):
#     summa += my_list[i]

print(my_list)
print(summa)

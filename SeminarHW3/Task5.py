# Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов (Негафибоначчи).

fib_pos = int(input('Введите желаемую позицию числа ряда Фибоначчи: '))

fib = [0]
fib1 = fib2 = 1

for i in range(fib_pos - 1):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    fib.append(fib_sum)
    fib.insert(0, fib_sum * ((-1)**(i + 1)))

print(fib)
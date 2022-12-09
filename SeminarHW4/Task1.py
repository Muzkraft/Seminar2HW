# А. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# B. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

from random import randint as rnd

def CreatePattern() -> dict:
    degree = int(input('Введите максимальную степень многочлена: '))

    equation_pattern = {}

    for key in range(degree, -1, -1):
        value = rnd(-100, 100)
        equation_pattern[key] = value

    return equation_pattern

def DecodeEquation(equation: dict) -> str:

    new_equation = ''
    first = True

    for (key, value) in equation.items():
        if value != 0:
            if first:
                if value > 0:
                    new_equation += f'{value}*x**{key} '
                else:
                    new_equation += f'-{value * (-1)}*x**{key} '
                first = False

            else:
                if value == 1:
                    if key == 1:
                        new_equation += f'+ x '
                    elif key == 0:
                        new_equation += f'+ 1'
                    else:
                        new_equation += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        new_equation += f'+ {value}*x '
                    elif key == 0:
                        new_equation += f'+ {value}'
                    else:
                        new_equation += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        new_equation += f'- x '
                    elif key == 0:
                        new_equation += f'- 1'
                    else:
                        new_equation += f'- x**{key} '

                elif value < 1:
                    if key == 1:
                        new_equation += f'- {value * (-1)}*x '
                    elif key == 0:
                        new_equation += f'- {value * (-1)}'
                    else:
                        new_equation += f'- {value * (-1)}*x**{key} '

    return new_equation + ' = 0'

def EncodeEquation(equation: str) -> dict:

    new_equation = []
    equation = equation.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')

    for item in equation:
        if not 'x' in item:
            new_equation.append([item, 0])
        else:
            if item.endswith('x'):
                if item == 'x':
                    new_equation.append(['1', '1'])
                elif item == '-x':
                    new_equation.append(['-1', '1'])
                else:
                    new_equation.append((item + '1').split('*x'))
            else:
                if item.startswith('x'):
                    new_equation.append(('1' + item).split('x**'))
                elif item.startswith('-x'):
                    new_equation.append(item.replace('-', '-1').split('x**'))
                else:
                    new_equation.append(item.split('*x**'))

        equation_pattern = {}

        for item in new_equation:
            equation_pattern[int(item[1])] = int(item[0])

        return equation_pattern

first = CreatePattern()
second = CreatePattern()

def EquationAddition(first: dict, second: dict) -> dict:
    base = {}
    base.update(first)
    base.update(second)

    for key in base:
        if first.get(key) and second.get(key):
            base[key] = first.get(key) + second.get(key)
        elif first.get(key):
            base[key] = first.get(key)
        else:
            base[key] = second.get(key)
    return dict(sorted(base.items())[::-1])

result = EquationAddition(first, second)

print(DecodeEquation(first))
print(DecodeEquation(second))
print(DecodeEquation(result))

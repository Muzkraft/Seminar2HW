from decimal import Decimal
import model
import operations
import string_calc
import view


def simple_calculate(first_number: Decimal):
    result = 0
    model.set_memory(first_number)
    while True:
        oper = view.input_operation()
        model.set_operation(oper)
        if oper == '=':
            break
        number = view.input_number('Введите число: ')
        model.set_number(number)

        first = model.get_memory()
        oper = model.get_operation()
        second = model.get_number()

        for operation in operations.operation:
            if oper == operation:
                result = operations.operation.get(oper)(first, second)
        view.print_result(result)
        model.set_memory(result)
        model.set_result(result)


def first_input():
    while True:
        number = view.first_input()
        number = number.strip().replace(' ', '').replace('+', ' + ').replace('-', ' - '). \
            replace('*', ' * ').replace('/', ' / ').replace('(', ' ( ').replace(')', ' ) ').split()
        if number[0] == '-':
            number[0] = number[0] + number[1]
            number.pop(1)
        if len(number) < 2:
            number = float(number[0])
            number = str(number)
            number = Decimal(number)
            simple_calculate(number)
            result = model.get_result()
        else:
            result = string_calc.eval_(number)

        view.print_result(result)
        retry = input('Посчитать еще одно выражение? (y/n)')
        if retry == 'n':
            break
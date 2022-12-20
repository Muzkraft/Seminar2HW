from decimal import Decimal
memory = 0
operation = ''
new_number = 0
result = 0


def get_memory():
    global memory
    return memory


def set_memory(value: Decimal):
    global memory
    memory = value


def get_result():
    global result
    return result


def set_result(value: Decimal):
    global result
    result = value


def get_operation():
    global operation
    return operation


def set_operation(value: str):
    global operation
    operation = value


def get_number():
    global new_number
    return new_number


def set_number(value: Decimal):
    global new_number
    new_number = value

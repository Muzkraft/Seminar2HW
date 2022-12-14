# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

data = input('Введите данные: ')

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding
    
with open('encode.txt', 'w') as file:
    file.write(rle_encode(data))




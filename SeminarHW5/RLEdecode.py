with open('encode.txt', 'r') as file:
    data = file.read()

def rle_decode(data):
    decode = ''
    count = ''

    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

decoded = rle_decode(data)

with open('decode.txt', 'w') as file:
    file.write(decoded)
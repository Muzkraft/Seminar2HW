# Написать программу, которая будет выводить в консоль заданный текст
# (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и
# удалять в заданном тексте все слова, в которых присутствует введенный шаблон.

orig_stroka = 'Python - один из самых популярных языков программирования в мире'

print(orig_stroka)

slova = orig_stroka.split(' ')

del_stroka = input('Введите подстроку: ')

new_slova = []

for slovo in slova:
    if del_stroka not in slovo:
        new_slova.append(slovo)

print(' '.join(new_slova))

"""
7)	Извлечь дату из строки. Формат даты dd –mm-yyyy (например, 2022-02-28).
8)	Найти все слова, в которых есть хотя бы одна буква ‘b’
"""
import re

test_string = "cat dog cat water 999 0 1 -2 456 z2krz z2222krz"
# 1) Вам дана строка. Выведите все подстроки, содержащие "cat".
pattern = r'cat'
for value in re.finditer(pattern, test_string):
    print(value)

# 2) Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
pattern = r'z\w{3}z'
for value in re.finditer(pattern, test_string):
    print(value)

# 3) Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров, и нужно проверить их,
# используя регулярные выражения в Python
numbers = ['1234567890', '8234567890', '9234567890', '1111111111', '0011223344']
pattern = r'^(8\d{9}$)|(9\d{9}$)'
for phone_number in numbers:
    for value in re.finditer(pattern, phone_number):
        print(value)

# 4) Дана строка, выведите все вхождения слов, начинающиеся на гласную букву.
# a e i o u y
new_test_string = "abc cow cat dog above orange ice"
pattern = r'\b[aoeiuy]\w+'
for value in re.finditer(pattern, new_test_string):
    print(value)

# 5) Дана строка. Вывести все числа этой строки, как отрицательные так и положительные.
new_test_string = "abc cow 52 -99 65461 3 -6 ice"
pattern = r'[-+]?\d+'
for value in re.finditer(pattern, new_test_string):
    print(value)

# 6) В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

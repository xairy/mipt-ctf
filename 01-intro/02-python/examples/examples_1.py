#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ввод-вывод. Числа, строки, bool. Конструкции if, for, while.

# Ввод-вывод cтрок.
first_word = raw_input()
second_word = raw_input()
spell = first_word + ' ' + second_word + '!'
print spell

# Ввод-вывод чисел.
first_number = int(raw_input())
second_number = float(raw_input())
print first_number + second_number

raw_input('Далее...\n')

# Смешанный вывод чисел и строк.
platform = first_number + second_number
print 'Платформа № ' + str(platform)
print "Платформа №", platform

raw_input('Далее...\n')

# Числа.
radius = 5
pi = 3.14159
square = pi * radius ** 2
print square
print 10 ** 100

raw_input('Далее...\n')

# Тип bool.
a = True
b = False
if a or b:
    print a and b

raw_input('Далее...\n')

# Коды символов.
a = ord('x')
print a
b = chr(a)
print b

raw_input('Далее...\n')

# Строки.
s = 'Tom Marvolo Riddle'
tokens = s.split()
first_name = tokens[0]
middle_name = tokens[1]
last_name = tokens[2]
s2 = first_name + ' ' + middle_name + ' ' + last_name

# Конструкция 'if'. Важно ставить отступы!
if (s == s2):
    print 'Две строки равны.'
else:
    print 'Так не бывает.'

raw_input('Далее...\n')

# Цикл 'for'. Отступы вновь важны!
for house in houses:
    print 'Ten points to', house, '!'

raw_input('Далее...\n')

# Цикл for для численного индекса.
s = ''
for i in range(5, 8):
    s += str(i)
print s

raw_input('Далее...\n')

# Цикл while.
number = 0
while True:
    number += 1
    if number == 42:
        break
print number

# Списки.
houses = ['Ravenclaw', 'Hufflepuff', 'Gryffindor']
houses.append('Slytherin')
print len(houses)

raw_input('Далее...\n')

# Сортировка.
houses.sort() # Сортировка на месте.
sorted_letters = sorted(houses[0]) # Новый список.
print houses
print sorted_letters

raw_input('Далее...\n')

# Кортеж / tuple.

t = (1, 'fish', 2, 'fish')

try:
  t[0] = 'red'
except:
  print 'Failed'

#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ввод-вывод cтрок.
first_word = raw_input()
second_word = raw_input()
spell = first_word + ' ' + second_word + '!'
print spell

raw_input('Далее...\n')

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

# Списки (изменяемые последовательности).
houses = ['Ravenclaw', 'Hufflepuff', 'Gryffindor']
houses.append('Slytherin')
print len(houses)

# Цикл 'for'. Отступы вновь важны!
for house in houses:
    print 'Ten points to', house, '!'

raw_input('Далее...\n')

# Set (неупорядоченные коллекции).
birth_name = 'Tom Marvolo Riddle'
birth_name_letters = set(birth_name)
birth_name_lower_letters = set(birth_name.lower())
nickname_lower_letters = set('I am Lord Voldemort'.lower())
print birth_name_lower_letters == nickname_lower_letters
print len(birth_name_lower_letters)

raw_input('Далее...\n')

fib_numbers = set([1, 1, 2, 3, 5, 8, 13, 21])
prime_numbers = set([2, 3, 5, 7, 11, 13, 17, 19])
union = fib_numbers | prime_numbers
intersection = fib_numbers & prime_numbers
difference = fib_numbers - prime_numbers
symmetric_difference = fib_numbers ^ prime_numbers

raw_input('Далее...\n')

# Проверка принадлежности.
print 3 in prime_numbers
print 4 in prime_numbers
print 'Griffindor' in houses
print 'ratio' in 'transfiguration'

raw_input('Далее...\n')

# Сортировка.
houses.sort() # Сортировка на месте.
sorted_letters = sorted(houses[0]) # Новый список.
print houses
print sorted_letters

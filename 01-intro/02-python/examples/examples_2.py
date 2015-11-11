#!/usr/bin/python
# -*- coding: utf-8 -*-

# Словарь, срезы, set.

# Словарь - соответствие из ключей в значения.
# Это как список, только индексы могут быть не только числами.
dictionary = {}
dictionary['half-blood'] = 'полукровка'
dictionary['cauldron'] = 'котёл'
dictionary['potion'] = 'зелье'
print dictionary['cauldron']
print 'potion' in dictionary
print 'зелье' in dictionary
print 'quidditch' in dictionary

raw_input('Далее...\n')

try:
    print dictionary['quidditch']
except KeyError as e:
    print 'Мы поймали исключение:', e

print dictionary.get('half-blood', 'неизвестно')
print dictionary.get('quidditch', 'неизвестно')

raw_input('Далее...\n')

# Всё нумеруется с нуля. Отрицательные индексы идут из конца в начало.
s = 'abcdefghi'
print s[0], s[1], s[-1], s[-2]

raw_input('Далее...\n')

# Типов переменных нет. Есть объекты и ссылки на них.
s = [5, 10, 'smth', {'A': 'a'}]
print s[0], s[1], s[-1], s[-2]
t = s
s.pop()
print s
print t

raw_input('Далее...\n')

# Есть срезы.
a = range(9, -1, -1)
print a
a = range(0, 10, 1)
a = range(0, 10)
a = range(10)
print a
b = a[3:6]
c = a[2:]
d = a[2::2]
e = a[6:3:-1]
f = a[6::-1]
g = a[::-1]
print 'b =', b
print 'c =', c
print 'd =', d
print 'e =', e
print 'f =', f
print 'g =', g

# Всё то же самое работает над строками.
a = 'abcdefghi'
b = a[3:6]
c = a[2:]
d = a[2::2]
e = a[6:3:-1]
f = a[6::-1]
g = a[::-1]

raw_input('Далее...\n')

# Создание двумерного списка.
a = [0] * 3
a[0] = 1
a[1] = 'a' * 5
print a

raw_input('Далее...\n')

# Создание двумерного списка.
a = [[None] * 3] * 2
a[0][0] = 'oops'
print a

raw_input('Далее...\n')

# Правильный способ.
a = [[None] * 3 for i in range(2)]
a[0][0] = 'oops'
print a

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

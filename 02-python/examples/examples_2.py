#!/usr/bin/python
# -*- coding: utf-8 -*-

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
print(s)
print(t)

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
print(a)

raw_input('Далее...\n')

# Кстати о range: тут так делают цикл for.
s = ''
for i in range(5, 8):
    s += str(i)
print s

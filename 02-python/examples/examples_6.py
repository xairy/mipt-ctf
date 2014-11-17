#!/usr/bin/python
# -*- coding: utf-8 -*-

# Map.

lst = [1, 2, 3]
double = lambda x: x * 2
print map(double, lst)

hello = map(ord, 'Hello World!')
print hello
print map(chr, hello)
print ''.join(map(chr, hello))

raw_input()


# Кортеж / tuple.

t = (1, 'fish', 2, 'fish')

try:
  t[0] = 'red'
except:
  print 'Failed'

raw_input()

# Zip.

lst1 = [1, 2]
lst2 = ['red', 'blue']
print zip(lst1, lst2)

raw_input()

# Filter.

lng = range(100)
print filter(lambda x: x > 50, lng)

raw_input()

# Hidden.

hidden = '666c61677b32313765303961666637636433346333346633376364313231346437663334377d'
print hidden[::2]
print hidden[1::2]
print zip(hidden[::2], hidden[1::2])
print map(lambda (x, y): x + y, zip(hidden[::2], hidden[1::2]))
print map(lambda (x, y): int(x + y, 16), zip(hidden[::2], hidden[1::2]))
print map(lambda (x, y): chr(int(x + y, 16)), zip(hidden[::2], hidden[1::2]))
print ''.join(map(lambda (x, y): chr(int(x + y, 16)), zip(hidden[::2], hidden[1::2])))

raw_input()

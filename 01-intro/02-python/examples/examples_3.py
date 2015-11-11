#!/usr/bin/python
# -*- coding: utf-8 -*-

# Функции, лямбда-функции. Сортировка по ключу.

# Функции объявляются через def, тело функции пишется с отступом.
def stats(seq):
    print ' '.join([str(i) for i in seq])
    print 'min: {0}, max: {1}'.format(min(seq), max(seq))

stats([3, 1, 5, 7, 4])
stats('Quirrel')

raw_input('Далее...\n')

f = lambda x, y: x + y
print f(3, 4)
print f([1, 2], [3, 4])
print f('ab', 'cd')

raw_input('Далее...\n')

# Можно сортировать по функции key. При сравнении сравниваются
# значения этой функции на элементах списка.
a = ['abc', 'abd', 'abcd', 'de', 'defgh', 'aaaaa', 'abcdef']
print min(a)
print max(a)
print min(a, key=lambda x: len(x))
print max(a, key=lambda x: len(x))
print min(a, key=len)
print max(a, key=len)
print sorted(a, key=len)
print sorted(a, key=max)
print sorted(a, key=lambda x: x[0])
print max(a, key=lambda x: x[0])
print sorted(a, key=lambda x: [len(x), x])
print max(a, key=lambda x: [len(x), x])
print sorted(a, key=len)
print sorted(a, key=lambda x: x[::-1])

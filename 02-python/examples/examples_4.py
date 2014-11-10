#!/usr/bin/python
# -*- coding: utf-8 -*-

# Так читать содержимое файла.
fin = open('input.txt')
for line in fin:
  print line.strip()
fin.close()

# Так в файл писать.
fout = open('output.txt', 'w')
fout.write('hello world')
fout.close()

# Чтобы не забыть закрыть файл.
with open('input.txt') as fin:
  for line in fin:
    print line.strip()

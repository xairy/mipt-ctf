#!/usr/bin/python
# -*- coding: utf-8 -*-

# Чтение и запись в файлы.

# Так читать содержимое файла.
fin = open('input.txt')
for line in fin:
  print line.strip()
fin.close()

raw_input('Далее...\n')

# Так в файл писать.
fout = open('output.txt', 'w')
fout.write('hello world')
fout.close()

raw_input('Далее...\n')

# Чтобы не забыть закрыть файл.
with open('input.txt') as fin:
  for line in fin:
    print line.strip()

raw_input('Далее...\n')

# Импортируем модуль sys.
import sys

# Чтение из стандартного входа и запись в стандартный выход.
# Ctrl+D чтобы завершить чтение.
for line in sys.stdin.readlines():
    sys.stdout.write(line)

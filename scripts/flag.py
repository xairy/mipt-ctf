#!/usr/bin/python3

import random
import sys

def random_hex_digit():
   return hex(random.randint(0x0, 0xf)).split('x')[1]

def random_hex_str(length):
  return ''.join([random_hex_digit() for i in range(length)])

def random_flag(length):
  return 'flag{' + random_hex_str(32) + '}'

if __name__ == '__main__':
  num = 1
  if len(sys.argv) == 2:
    num = int(sys.argv[1])
  for i in range(num):
    print(random_flag(32))

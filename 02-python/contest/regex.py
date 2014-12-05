#!/usr/bin/python

import re

with open('input.txt') as fin:
  for line in fin:
    for match in re.findall('flag\{[0-9a-z]{32}\}', line):
      print match

#!/usr/bin/python
# -*- coding: utf-8 -*-

print "What files do you want?"

files = input('list> ')

for name in files:
  try:
    with open(name) as f:
      print f.read()
  except:
    print name, "does not exist!"

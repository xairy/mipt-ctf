#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print "What files do you want?"

files = input('list> ')

for name in files:
  if os.path.exists(name):
    with open(name) as f:
      print f.read()
  else:
    print name, "does not exist!"

#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print locals()
print globals()

print dir(os)
print dir([])

print vars(os)
print os.__dict__

print dir(__builtins__)
print __builtins__.__dict__

del __builtins__.__dict__['__import__']

try:
  sys = __import__('sys')
except:
  print 'Failed'

print dir(os)
sys = os.sys

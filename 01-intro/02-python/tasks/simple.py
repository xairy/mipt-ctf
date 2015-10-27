#!/usr/bin/python

line = raw_input()

if line[0::2] != 'faa8babcb4d573f1':
  print 'Fail!'
  exit(0)

if line[-1:0:-2] != 'bec86ad48f2419bf':
  print 'Fail!'
  exit(0)

print 'Success!'

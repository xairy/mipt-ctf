#!/usr/bin/python -u
# task5.py
# A real challenge for those python masters out there :)

from sys import modules
modules.clear()
del modules

_raw_input = raw_input
_BaseException = BaseException
_EOFError = EOFError

__builtins__.__dict__.clear()
__builtins__ = None

print 'Get a shell, if you can...'

while 1:
  try:
    d = {'x':None}
    exec 'x='+_raw_input()[:50] in d
    print 'Return Value:', d['x']
  except _EOFError, e:
    raise e
  except _BaseException, e:
    print 'Exception:', e

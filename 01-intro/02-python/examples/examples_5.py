#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

line = 'Cats are smarter than dogs'


# Searching one.

search = re.search('[^ ]+', line)

if search:
   print 'Found by search:', search.group()
else:
   print 'Nothing found!'

raw_input()


# Searching many.

findall = re.findall('[^ ]+', line)
for match in findall:
  print 'Found by findall:', match

raw_input()


# Matching.

match = re.match('(.+) are [^ ]+ than (.+)', line)

if match:
   print 'Matched:', match.group()
   print 'match.group(0):', match.group(1)
   print 'match.group(1):', match.group(2)
else:
   print 'No match!'

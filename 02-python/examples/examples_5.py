#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

line = "Cats are smarter than dogs"

match = re.match('(.*) are ([a-z]+) (.*)', line)

if match:
   print "match.group() :", match.group()
   print "match.group(1):", match.group(1)
   print "match.group(2):", match.group(2)
   print "match.group(3):", match.group(3)
else:
   print "No match!"


search = re.search('[^ ]+', line)

if search:
   print "search.group():", search.group()
else:
   print "Nothing found!"

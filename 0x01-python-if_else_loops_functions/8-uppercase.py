#!/usr/bin/python3
def uppercase(str):
    transformed = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            transformed += chr(ord(c) - 32)
        else:
            transformed += c
    print(str)

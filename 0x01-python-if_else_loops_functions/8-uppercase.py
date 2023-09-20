#!/usr/bin/python3

def uppercase(str):
    for i in str:
        if 'a' <= i <= 'z':
            _upper = chr(ord(i) - 32)
            print("{}".format(_upper), end='')
        else:
            print("{}".format(i), end='')
    print("")

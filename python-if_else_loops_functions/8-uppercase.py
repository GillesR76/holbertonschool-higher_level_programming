#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 97 and ord(i) <= 122):
            j = ord(i) - 32
            print("{}".format(chr(j)), end="")
        else:
            print(i, end="")
    print()

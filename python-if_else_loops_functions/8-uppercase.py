#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            result += chr(ord(str[i]) - 32)
        else:
            result += str[i]
    print("{}".format(result))

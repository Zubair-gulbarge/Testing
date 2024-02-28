# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

def reverse_integer(x):
    if x >= 0:
        rev = int(str(x)[::-1])
    else:
        rev = -int(str(-x)[::-1])
    return rev if -(2**31) <= rev <= (2**31 - 1) else 0

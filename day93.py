# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

def reverse_integer(x):
    sign = 1 if x >= 0 else -1
    x = abs(x)
    rev = 0
    while x != 0:
        pop = x % 10
        x //= 10
        rev = rev * 10 + pop
    rev *= sign
    if rev < -2**31 or rev > 2**31 - 1:
        return 0
    return rev

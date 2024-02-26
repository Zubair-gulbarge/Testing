# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

# def reverse_integer(x):
#     sign = -1 if x < 0 else 1
#     x *= sign
#     reversed_int = 0
#     while x:
#         reversed_int = reversed_int * 10 + x % 10
#         x //= 10
#     if reversed_int > 2**31 - 1:
#         return 0
#     return reversed_int * sign

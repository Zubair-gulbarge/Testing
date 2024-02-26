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

# Problem: Valid Parentheses
# Description: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Code:

# def is_valid(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack

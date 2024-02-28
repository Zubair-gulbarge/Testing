# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

# def reverse_integer(x):
#     if x >= 0:
#         rev = int(str(x)[::-1])
#     else:
#         rev = -int(str(-x)[::-1])
#     return rev if -(2**31) <= rev <= (2**31 - 1) else 0

# Problem: Palindrome Number
# Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Code:

# def is_palindrome(x):
#     if x < 0:
#         return False
#     return str(x) == str(x)[::-1]

# Problem: Valid Parentheses
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
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

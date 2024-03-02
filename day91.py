# Problem: Valid Parentheses
# Description: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Code:

# def is_valid(s):
#     stack = []
#     mapping = {")": "(", "}": "{", "]": "["}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack

# Problem: Reverse Integer
# Description: Given a signed 32-bit integer x, return x with its digits reversed.
# Code:

# def reverse(x):
#     sign = [1, -1][x < 0]
#     x = abs(x)
#     reversed_x = int(str(x)[::-1]) * sign
#     return reversed_x if -(2**31)-1 < reversed_x < 2**31 else 0

# Problem: Implement strStr()
# Description: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Code:

def str_str(haystack, needle):
    if not needle:
        return 0
    if needle not in haystack:
        return -1
    return haystack.index(needle)

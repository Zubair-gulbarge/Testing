# Problem: Longest Common Prefix
# Description: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
# Code:

# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     min_str = min(strs, key=len)
#     for i, char in enumerate(min_str):
#         for other in strs:
#             if other[i] != char:
#                 return min_str[:i]
#     return min_str

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

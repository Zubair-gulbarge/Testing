# Problem: Longest Common Prefix
# Description: Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
# Code:

# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     min_str = min(strs, key=len)
#     for i, char in enumerate(min_str):
#         for string in strs:
#             if string[i] != char:
#                 return min_str[:i]
#     return min_str

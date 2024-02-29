# Problem: Two Sum
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Code:

# def two_sum(nums, target):
#     num_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in num_map:
#             return [num_map[complement], i]
#         num_map[num] = i
#     return []

# Problem: Roman to Integer
# Description: Given a roman numeral, convert it to an integer.
# Code:

# def roman_to_int(s):
#     roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     prev_value = 0
#     for char in reversed(s):
#         value = roman_map[char]
#         if value < prev_value:
#             result -= value
#         else:
#             result += value
#         prev_value = value
#     return result

# Problem: Longest Common Prefix
# Description: Write a function to find the longest common prefix string amongst an array of strings.
# Code:

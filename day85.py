# Problem: Check for Anagrams
# Description: Write a function to check if two strings are anagrams of each other.
# Code:

# def check_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)

# Problem: Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Code:

# def missing_number(nums):
#     n = len(nums)
#     total_sum = n * (n + 1) // 2
#     return total_sum - sum(nums)

# Problem: Reverse Words in a String
# Description: Given an input string, reverse the string word by word.
# Code:

# def reverse_words(s):
#     return ' '.join(s.split()[::-1])

# Problem: Rotate Array
# Description: Rotate an array to the right by k steps, where k is non-negative.
# Code:

# def rotate_array(nums, k):
#     k %= len(nums)
#     nums[:] = nums[-k:] + nums[:-k]

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

# Problem: Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Code:

# def missing_number(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

# Problem: Check if Two Strings are Anagrams
# Description: Given two strings, check if they are anagrams of each other.
# Code:

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

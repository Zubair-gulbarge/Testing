# Problem: Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Code:

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

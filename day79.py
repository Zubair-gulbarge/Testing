# Problem: Find the Missing Number in a List
# Description: Given a list of integers from 1 to n with one missing number, find the missing number.
# Code:

def find_missing_number(nums):
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

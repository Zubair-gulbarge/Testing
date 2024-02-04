# Problem: Find the Longest Increasing Subsequence
# Description: Given an array of integers, find the length of the longest increasing subsequence.
# Code:

# def length_of_lis(nums):
#     if not nums:
#         return 0
#     dp = [1] * len(nums)
#     for i in range(1, len(nums)):
#         for j in range(i):
#             if nums[i] > nums[j]:
#                 dp[i] = max(dp[i], dp[j] + 1)
#     return max(dp)

# Problem: Find the Maximum Subarray Sum
# Description: Given an array of integers, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.
# Code:

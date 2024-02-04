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

# def max_subarray_sum(nums):
#     if not nums:
#         return 0
#     max_sum = current_sum = nums[0]
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# Problem: Implement a Trie (Prefix Tree)
# Description: Implement a trie data structure that supports insertion of words and searching for words.
# Code:

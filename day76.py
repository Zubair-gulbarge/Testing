# Problem: Implement Insertion Sort
# Description: Implement the insertion sort algorithm to sort an array of integers.
# Code:

# def insertion_sort(nums):
#     for i in range(1, len(nums)):
#         key = nums[i]
#         j = i - 1
#         while j >= 0 and key < nums[j]:
#             nums[j + 1] = nums[j]
#             j -= 1
#         nums[j + 1] = key
#     return nums

# Problem: Check if a String is a Palindrome
# Description: Determine if a given string is a palindrome.
# Code:

# def is_palindrome(s):
#     s = ''.join(c.lower() for c in s if c.isalnum())
#     return s == s[::-1]

# Problem: Find the Maximum Subarray Sum
# Description: Given an integer array, find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.
# Code:

# def max_subarray_sum(nums):
#     max_sum = current_sum = nums[0]
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# Problem: Implement Quick Sort
# Description: Implement the quick sort algorithm to sort an array of integers.
# Code:

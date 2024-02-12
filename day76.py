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

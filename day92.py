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

# Problem: Merge Two Sorted Lists
# Description: Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
# Code:

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1, l2):
#     if not l1:
#         return l2
#     if not l2:
#         return l1
#     if l1.val < l2.val:
#         l1.next = merge_two_lists(l1.next, l2)
#         return l1
#     else:
#         l2.next = merge_two_lists(l1, l2.next)
#         return l2

# Problem: Remove Duplicates from Sorted Array
# Description: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Code:

# def remove_duplicates(nums):
#     if not nums:
#         return 0
#     unique_index = 0
#     for i in range(1, len(nums)):
#         if nums[i] != nums[unique_index]:
#             unique_index += 1
#             nums[unique_index] = nums[i]
#     return unique_index + 1

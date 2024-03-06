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

# Problem: Merge Two Sorted Lists
# Description: Merge two sorted linked lists and return it as a new sorted list.
# Code:

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1, l2):
#     dummy = ListNode(0)
#     current = dummy
#     while l1 and l2:
#         if l1.val < l2.val:
#             current.next = l1
#             l1 = l1.next
#         else:
#             current.next = l2
#             l2 = l2.next
#         current = current.next
#     current.next = l1 if l1 else l2
#     return dummy.next

# Problem: First Unique Character in a String
# Description: Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Code:

# def first_uniq_char(s):
#     char_count = {}
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
#     for i, char in enumerate(s):
#         if char_count[char] == 1:
#             return i
#     return -1

# Problem: Maximum Subarray
# Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Code:

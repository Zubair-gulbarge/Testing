# Problem: Merge Two Sorted Lists
# Description: Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
# Code:

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def merge_two_lists(l1, l2):
#     dummy = ListNode()
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

# Problem: Two Sum
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Code:

# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i

# Problem: Maximum Subarray
# Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Code:

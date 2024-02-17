# Problem: Reverse a Linked List
# Description: Reverse a singly linked list.
# Code:

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def reverse_linked_list(head):
#     prev = None
#     curr = head
#     while curr:
#         next_node = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next_node
#     return prev

# Problem: Implement Binary Search
# Description: Implement the binary search algorithm to find the index of a target element in a sorted list.
# Code:

def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

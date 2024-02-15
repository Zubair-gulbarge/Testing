# Problem: Find the Missing Number in a List
# Description: Given a list of integers from 1 to n with one missing number, find the missing number.
# Code:

# def find_missing_number(nums):
#     n = len(nums) + 1
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

# Problem: Implement Merge Sort
# Description: Implement the Merge Sort algorithm to sort a list of integers.
# Code:

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])
#     return merge(left_half, right_half)

# def merge(left, right):
#     merged = []
#     l, r = 0, 0
#     while l < len(left) and r < len(right):
#         if left[l] < right[r]:
#             merged.append(left[l])
#             l += 1
#         else:
#             merged.append(right[r])
#             r += 1
#     merged.extend(left[l:])
#     merged.extend(right[r:])
#     return merged

# Problem: Check if a Binary Tree is a Binary Search Tree (BST)
# Description: Given a binary tree, determine if it is a Binary Search Tree.
# Code:

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not min_val < root.val < max_val:
        return False
    return is_bst(root.left, min_val, root.val) and is_bst(root.right, root.val, max_val)

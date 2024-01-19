# Problem: Quick Sort

# Description: Implement the quick sort algorithm.
# Code:

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left = [x for x in arr[1:] if x <= pivot]
#         right = [x for x in arr[1:] if x > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)

# Problem: Stack Implementation

# Description: Implement a stack data structure.
# Code:

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

# Problem: Merge Sort

# Description: Implement the merge sort algorithm.
# Code:

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i, j, k = 0, 0, 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

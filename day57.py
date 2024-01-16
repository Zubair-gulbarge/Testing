# Problem: Binary Search

# Description: Implement the binary search algorithm.
# Code:

# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# Problem: Bubble Sort

# Description: Implement the bubble sort algorithm.
# Code:

# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

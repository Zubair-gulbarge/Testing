# Problem: Implement Binary Search
# Description: Implement the binary search algorithm to find the index of a target element in a sorted array.
# Code:

# def binary_search(nums, target):
#     left, right = 0, len(nums) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# Problem: Implement Selection Sort
# Description: Implement the selection sort algorithm to sort an array of integers.
# Code:

# def selection_sort(nums):
#     for i in range(len(nums)):
#         min_index = i
#         for j in range(i + 1, len(nums)):
#             if nums[j] < nums[min_index]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums

# Problem: Rotate Array
# Description: Given an array, rotate the array to the right by k steps, where k is non-negative.
# Code:

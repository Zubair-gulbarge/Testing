# def max_subarray_sum(arr):
#     max_sum = float('-inf')
#     current_sum = 0
    
#     for num in arr:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
    
#     return max_sum

# # Example usage
# input_list = [1, -2, 3, 4, -1, 2, 1, -5, 4]
# result = max_subarray_sum(input_list)
# print("Maximum subarray sum:", result)

# Problem: Merge Sort Implementation
# Description: Implement the merge sort algorithm to sort an array of integers.
# Code:

# def merge_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) // 2
#     left = merge_sort(nums[:mid])
#     right = merge_sort(nums[mid:])
#     return merge(left, right)

# def merge(left, right):
#     merged = []
#     left_index, right_index = 0, 0
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             merged.append(left[left_index])
#             left_index += 1
#         else:
#             merged.append(right[right_index])
#             right_index += 1
#     merged.extend(left[left_index:])
#     merged.extend(right[right_index:])
#     return merged

# Problem: Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Code:

# def missing_number(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

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
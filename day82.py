# Problem: Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Code:

# def missing_number(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     actual_sum = sum(nums)
#     return expected_sum - actual_sum

# Problem: Check if Two Strings are Anagrams
# Description: Given two strings, check if they are anagrams of each other.
# Code:

# def are_anagrams(s1, s2):
#     return sorted(s1) == sorted(s2)

# Problem: Implement a Stack Using Lists
# Description: Implement a stack data structure using Python lists.
# Code:

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

#     def peek(self):
#         return self.items[-1]

#     def size(self):
#         return len(self.items)

# Problem: Implement Quick Sort
# Description: Implement the quick sort algorithm to sort a list of numbers.
# Code:

# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = [x for x in nums if x < pivot]
#     middle = [x for x in nums if x == pivot]
#     right = [x for x in nums if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# Problem: Find the Intersection of Two Arrays
# Description: Given two arrays, write a function to compute their intersection.
# Code:

# def intersection(nums1, nums2):
#     return list(set(nums1) & set(nums2))

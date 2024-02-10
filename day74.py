# Problem: Merge Two Sorted Arrays
# Description: Given two sorted arrays nums1 and nums2, merge them into a single sorted array.
# Code:

# def merge_sorted_arrays(nums1, m, nums2, n):
#     i, j, k = m - 1, n - 1, m + n - 1
#     while i >= 0 and j >= 0:
#         if nums1[i] > nums2[j]:
#             nums1[k] = nums1[i]
#             i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1
#         k -= 1
#     while j >= 0:
#         nums1[k] = nums2[j]
#         j -= 1
#         k -= 1

# Problem: Counting Sort
# Description: Implement the counting sort algorithm to sort an array of integers.
# Code:

# def counting_sort(nums):
#     max_num = max(nums)
#     count = [0] * (max_num + 1)
#     for num in nums:
#         count[num] += 1
#     result = []
#     for i in range(len(count)):
#         result.extend([i] * count[i])
#     return result

# Problem: Implement Quick Sort
# Description: Implement the quick sort algorithm to sort an array of integers.
# Code:

# def quick_sort(nums):
#     if len(nums) <= 1:
#         return nums
#     pivot = nums[len(nums) // 2]
#     left = [x for x in nums if x < pivot]
#     middle = [x for x in nums if x == pivot]
#     right = [x for x in nums if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# Problem: Find All Anagrams in a String
# Description: Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Code:

from collections import Counter
def find_anagrams(s, p):
    result = []
    p_count = Counter(p)
    s_count = Counter(s[:len(p)-1])
    for i in range(len(p)-1, len(s)):
        s_count[s[i]] += 1
        if s_count == p_count:
            result.append(i - len(p) + 1)
        s_count[s[i - len(p) + 1]] -= 1
        if s_count[s[i - len(p) + 1]] == 0:
            del s_count[s[i - len(p) + 1]]
    return result

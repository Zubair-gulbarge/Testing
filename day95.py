# Problem: Merge Intervals
# Description: Given a collection of intervals, merge all overlapping intervals.
# Code:

# def merge(intervals):
#     if not intervals:
#         return []
#     intervals.sort(key=lambda x: x[0])
#     merged = [intervals[0]]
#     for interval in intervals[1:]:
#         if interval[0] <= merged[-1][1]:
#             merged[-1][1] = max(merged[-1][1], interval[1])
#         else:
#             merged.append(interval)
#     return merged

# Problem: Reverse Integer
# Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
# Code:

# def reverse(x):
#     if x < 0:
#         sign = -1
#         x = -x
#     else:
#         sign = 1
#     reversed_x = int(str(x)[::-1])
#     if reversed_x > 2**31 - 1:
#         return 0
#     return sign * reversed_x

# Problem: Two Sum
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Code:

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

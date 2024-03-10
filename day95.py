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

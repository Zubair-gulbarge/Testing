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

#         i = j = k = 0

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

def binary_search(arr, low, high, x):
    """Helper function for finding insertion point of a sorted array."""
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
            # If element is smaller than mid, then it can only be present in left subarray
        elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
                # Else the element can only be present in the right subarray
        else:
                return binary_search(arr, mid + 1, high, x)
    else:
                return -1
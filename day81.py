# Problem: Calculate the Fibonacci Sequence
# Description: Generate the Fibonacci sequence up to a specified number of terms.
# Code:

# def fibonacci(n):
#     fib = [0, 1]
#     while len(fib) < n:
#         fib.append(fib[-1] + fib[-2])
#     return fib[:n]

# Problem: Find the Maximum Subarray Sum
# Description: Find the contiguous subarray within a one-dimensional array of numbers that has the largest sum.
# Code:

# def max_subarray_sum(nums):
#     max_sum = curr_sum = nums[0]
#     for num in nums[1:]:
#         curr_sum = max(num, curr_sum + num)
#         max_sum = max(max_sum, curr_sum)
#     return max_sum

# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

# def reverse_integer(x):
#     sign = -1 if x < 0 else 1
#     x *= sign
#     reversed_int = 0
#     while x:
#         reversed_int = reversed_int * 10 + x % 10
#         x //= 10
#     if reversed_int > 2**31 - 1:
#         return 0
#     return reversed_int * sign

# Problem: Valid Parentheses
# Description: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Code:

# def is_valid(s):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#     for char in s:
#         if char in mapping:
#             top_element = stack.pop() if stack else '#'
#             if mapping[char] != top_element:
#                 return False
#         else:
#             stack.append(char)
#     return not stack

# Problem: Climbing Stairs
# Description: You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Code:

# def climb_stairs(n):
#     if n <= 2:
#         return n
#     prev, curr = 1, 2
#     for _ in range(3, n + 1):
#         prev, curr = curr, prev + curr
#     return curr

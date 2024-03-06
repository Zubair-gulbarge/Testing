# Problem: Reverse Integer
# Description: Given a 32-bit signed integer, reverse digits of an integer.
# Code:

# def reverse_integer(x):
#     sign = 1 if x >= 0 else -1
#     x = abs(x)
#     rev = 0
#     while x != 0:
#         pop = x % 10
#         x //= 10
#         rev = rev * 10 + pop
#     rev *= sign
#     if rev < -2**31 or rev > 2**31 - 1:
#         return 0
#     return rev

# Problem: Palindrome Number
# Description: Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
# Code:

# def is_palindrome(x):
#     if x < 0:
#         return False
#     reversed_x = int(str(x)[::-1])
#     return x == reversed_x

# Problem: Two Sum
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Code:

def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return None

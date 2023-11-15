# def two_sum(nums, target):
#     complement_dict = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in complement_dict:
#             return [complement_dict[complement], i]
#         complement_dict[num] = i
#     return None

# def reverse_integer(x):
#     INT_MAX, INT_MIN = 2**31 - 1, -2**31
#     result = 0
#     sign = 1 if x >= 0 else -1
#     x = abs(x)

#     while x != 0:
#         pop = x % 10
#         x //= 10

#         if result > (INT_MAX - pop) // 10:
#             return 0

#         result = result * 10 + pop

#     return sign * result

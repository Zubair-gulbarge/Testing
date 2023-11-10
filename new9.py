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

# def is_palindrome(x):
#     if x < 0 or (x % 10 == 0 and x != 0):
#         return False

#     reversed_num = 0
#     while x > reversed_num:
#         reversed_num = reversed_num * 10 + x % 10
#         x //= 10

#     return x == reversed_num or x == reversed_num // 10

def roman_to_int(s):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in reversed(s):
        current_value = roman_dict[char]

        if current_value >= prev_value:
            result += current_value
        else:
            result -= current_value

        prev_value = current_value

    return result

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# # Example usage:
# n = 5
# result = factorial(n)
# print(f"The factorial of {n} is: {result}")

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# # Example usage:
# number = 13
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# def fibonacci(n):
#     fib_sequence = [0, 1]
#     while len(fib_sequence) < n:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

# # Example usage:
# n = 8
# result = fibonacci(n)
# print(f"The first {n} numbers in the Fibonacci series are: {result}")

# def reverse_string(s):
#     return s[::-1]

# # Example usage:
# input_str = "Python"
# result = reverse_string(input_str)
# print(f"The reversed string is: {result}")

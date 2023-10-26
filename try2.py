# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# # Test the function
# number = int(input("Enter a non-negative integer: "))
# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(number)
#     print(f"The factorial of {number} is {result}")

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test the function
num1 = int(input("Enter the first positive integer: "))
num2 = int(input("Enter the second positive integer: "))

if num1 <= 0 or num2 <= 0:
    print("Both numbers should be positive integers.")
else:
    result = gcd(num1, num2)
    print(f"The GCD of {num1} and {num2} is {result}")

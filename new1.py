# import math

# # Get the radius from the user
# radius = float(input("Enter the radius of the circle: "))

# # Calculate the area of the circle
# area = math.pi * (radius ** 2)

# # Print the result
# print(f"The area of the circle with radius {radius} is {area:.2f}")

# # Get a string from the user
# text = input("Enter a string: ")

# # Count vowels and consonants
# vowels = 0
# consonants = 0

# for char in text:
#     if char.isalpha():
#         if char.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# # Print the counts
# print(f"Vowels: {vowels}, Consonants: {consonants}")

# Get a positive integer from the user
# number = int(input("Enter a positive integer: "))

# # Calculate the sum of its digits
# digit_sum = 0
# while number > 0:
#     digit_sum += number % 10
#     number //= 10

# # Print the sum of digits
# print(f"The sum of digits is: {digit_sum}")

# Generate the first n terms of the Fibonacci sequence
# n = int(input("Enter the number of terms: "))

# a, b = 0, 1
# fib_sequence = []

# for _ in range(n):
#     fib_sequence.append(a)
#     a, b = b, a + b

# print(f"The first {n} terms of the Fibonacci sequence are: {fib_sequence}")

# Get a string from the user
# input_string = input("Enter a string: ")

# # Reverse the string
# reversed_string = input_string[::-1]

# # Print the reversed string
# print(f"The reversed string is: {reversed_string}")

# Check if a number is prime
num = int(input("Enter a positive integer: "))

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

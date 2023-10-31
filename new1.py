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
number = int(input("Enter a positive integer: "))

# Calculate the sum of its digits
digit_sum = 0
while number > 0:
    digit_sum += number % 10
    number //= 10

# Print the sum of digits
print(f"The sum of digits is: {digit_sum}")

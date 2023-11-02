# # Reverse a list
# original_list = [1, 2, 3, 4, 5]

# reversed_list = original_list[::-1]

# print(f"The reversed list is: {reversed_list}")

# Check if a number is an Armstrong number
# number = int(input("Enter a positive integer: "))

# Calculate the power of a number
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

result = base ** exponent

print(f"{base} raised to the power of {exponent} is {result}")


# def is_armstrong(num):
#     order = len(str(num))
#     total = 0
#     temp = num

#     while temp > 0:
#         digit = temp % 10
#         total += digit ** order
#         temp //= 10

#     return num == total

# if is_armstrong(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")



# # Calculating the factorial of a number using a while loop
# num = int(input("Enter a number: "))
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print("Factorial:", factorial)

# Printing a pattern using nested for loops
# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Simple password verification using a while loop
# password = "secret"
# user_input = input("Enter the password: ")
# while user_input != password:
#     print("Incorrect password. Try again.")
#     user_input = input("Enter the password: ")
# print("Access granted!")

# Finding prime numbers in a given range using a for loop
# start = 10
# end = 20
# print("Prime numbers between", start, "and", end, "are:")
# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, int(num**0.5) + 1):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

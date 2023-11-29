# Checking if a number is prime using a while loop
# number = 17
# is_prime = True
# divisor = 2

# while divisor <= number // 2:
#     if number % divisor == 0:
#         is_prime = False
#         break
#     divisor += 1

# if is_prime:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# Printing a reverse triangle pattern using a nested for loop
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Calculating the factorial of a number using a while loop
n = 5
factorial = 1
current = 1

while current <= n:
    factorial *= current
    current += 1

print(f"The factorial of {n} is: {factorial}")

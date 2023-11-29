# Checking if a number is prime using a while loop
number = 17
is_prime = True
divisor = 2

while divisor <= number // 2:
    if number % divisor == 0:
        is_prime = False
        break
    divisor += 1

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

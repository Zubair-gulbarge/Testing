def prime_factors(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

# Test the function
number = int(input("Enter a positive integer: "))

if number <= 0:
    print("Please enter a positive integer.")
else:
    factors = prime_factors(number)
    if len(factors) == 1:
        print(f"{number} is a prime number.")
    else:
        print(f"The prime factors of {number} are: {', '.join(map(str, factors))}")

# Find the factors of a positive integer
number = int(input("Enter a positive integer: "))

factors = []

for i in range(1, number + 1):
    if number % i == 0:
        factors.append(i)

print(f"The factors of {number} are: {factors}")

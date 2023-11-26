# Calculating the power of a number using a while loop
base = 2
exponent = 5
result = 1

while exponent > 0:
    result *= base
    exponent -= 1

print(f"{base} raised to the power of {exponent}: {result}")

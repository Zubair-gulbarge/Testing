# Taking multiple integer inputs in a loop
n = int(input("Enter the number of values: "))
values = []
for _ in range(n):
    value = int(input("Enter a value: "))
    values.append(value)

# Example: Input: 3, followed by three values
print(values)

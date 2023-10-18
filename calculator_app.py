# calculator_app.py
import calculator

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations using the functions from calculator.py
sum_result = calculator.add(num1, num2)
difference_result = calculator.subtract(num1, num2)
product_result = calculator.multiply(num1, num2)
division_result = calculator.divide(num1, num2)

# Display the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
    
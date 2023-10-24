# BMI Calculator

# Input weight and height from the user
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = weight_kg / (height_m ** 2)

# Print the BMI
print("Your BMI is:", round(bmi, 2))

# Interpret the BMI
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your weight is normal.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

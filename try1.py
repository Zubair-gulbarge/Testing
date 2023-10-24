# # BMI Calculator

# # Input weight and height from the user
# weight_kg = float(input("Enter your weight in kilograms: "))
# height_m = float(input("Enter your height in meters: "))

# # Calculate BMI
# bmi = weight_kg / (height_m ** 2)

# # Print the BMI
# print("Your BMI is:", round(bmi, 2))

# # Interpret the BMI
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("Your weight is normal.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")

# Start
# Initialize an empty string variable for the alphabet list.
alphabet_list = "abcdefghijklmnopqrstuvwxyz"

# Initialize a dictionary to store letter frequencies.
letter_frequencies = {}

# Loop through each letter in the alphabet list:
for letter in alphabet_list:
    # Create a variable to store the frequency and set it to zero.
    frequency = 0

    # Loop through each letter in the given string:
    given_string = "Your input string goes here"
    for char in given_string:
        # If the letter in the string is the same as the current letter in the alphabet list:
        if char == letter:
            # Increase the frequency variable by one.
            frequency += 1

    # If the frequency variable is not zero:
    if frequency != 0:
        # Print the current letter in the alphabet list followed by a colon and the value of the frequency variable.
        print(f"{letter}: {frequency}")

# End

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

# def is_palindrome(string):
#     # Remove spaces and convert to lowercase for case-insensitive comparison
#     cleaned_string = string.replace(" ", "").lower()
#     # Compare the original string with its reverse
#     return cleaned_string == cleaned_string[::-1]

# # Test the function
# input_string = input("Enter a string: ")

# if is_palindrome(input_string):
#     print("It's a palindrome.")
# else:
#     print("It's not a palindrome.")

# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase for case-insensitive comparison
#     cleaned_str1 = str1.replace(" ", "").lower()
#     cleaned_str2 = str2.replace(" ", "").lower()

#     # Check if the sorted characters of the cleaned strings are the same
#     return sorted(cleaned_str1) == sorted(cleaned_str2)

# # Test the function
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# if are_anagrams(string1, string2):
#     print("These strings are anagrams of each other.")
# else:
#     print("These strings are not anagrams.")

def remove_duplicates(input_list):
    seen = set()
    unique_list = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)

    return unique_list

# Test the function
input_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_items = remove_duplicates(input_list)
print("Original List:", input_list)
print("List with Duplicates Removed:", unique_items)

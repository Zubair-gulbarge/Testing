# # Simple number guessing game using a while loop
# import random

# target_number = random.randint(1, 20)
# guess = 0

# while guess != target_number:
#     guess = int(input("Guess the number (between 1 and 20): "))
#     if guess < target_number:
#         print("Too low. Try again.")
#     elif guess > target_number:
#         print("Too high. Try again.")

# print("Congratulations! You guessed the correct number:", target_number)

# Iterating over a dictionary using a for loop
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
for name, grade in student_grades.items():
    print(f"{name}'s grade: {grade}")

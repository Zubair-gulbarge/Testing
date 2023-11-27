# Printing a pattern using a nested for loop
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()

# Checking if a word is a palindrome using a while loop
# word = "radar"
# original_word = word.lower()
# reversed_word = ""

# while original_word:
#     reversed_word += original_word[-1]
#     original_word = original_word[:-1]

# if word.lower() == reversed_word:
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")

# Checking if a word is a palindrome using a while loop
word = "radar"
original_word = word.lower()
reversed_word = ""

while original_word:
    reversed_word += original_word[-1]
    original_word = original_word[:-1]

if word.lower() == reversed_word:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

alphabet_list = "abcdefghijklmnopqrstuvwxyz"
letter_frequencies = {}
for letter in alphabet_list:
    frequency = 0
    given_string = "You can have data without information, but you cannot have information without data."
    for char in given_string:
        if char == letter:
            frequency += 1
    if frequency != 0:
        print(f"{letter}: {frequency}")
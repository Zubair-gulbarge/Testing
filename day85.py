# Problem: Check for Anagrams
# Description: Write a function to check if two strings are anagrams of each other.
# Code:

def check_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

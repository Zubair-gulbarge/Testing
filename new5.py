# from collections import defaultdict

# def group_anagrams(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         sorted_word = "".join(sorted(word))
#         anagrams[sorted_word].append(word)
#     return list(anagrams.values())

# # Example usage:
# word_list = ["listen", "silent", "hello", "world", "evil", "vile"]
# anagram_groups = group_anagrams(word_list)
# print("Anagram Groups:", anagram_groups)

# import requests
# from bs4 import BeautifulSoup

# url = "https://quotes.toscrape.com/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# quotes = soup.find_all("span", class_="text")
# for quote in quotes:
#     print(quote.get_text())

def calculator():
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operator"

    print(f"Result: {result}")

# Example usage:
calculator()

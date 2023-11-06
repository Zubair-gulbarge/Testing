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

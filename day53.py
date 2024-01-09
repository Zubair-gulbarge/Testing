# Problem: Natural Language Processing with NLTK
# - Description: Use the Natural Language Toolkit (NLTK) for basic text processing tasks.
# - Code:

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist

# # Download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

# # Sample text
# text = "Natural Language Processing is a subfield of artificial intelligence."

# # Tokenization
# words = word_tokenize(text)

# # Remove stop words
# stop_words = set(stopwords.words('english'))
# filtered_words = [word for word in words if word.lower() not in stop_words]

# # Frequency distribution
# freq_dist = FreqDist(filtered_words)
# print(freq_dist)

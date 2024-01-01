# Problem: Asynchronous Programming with Asyncio
# Description: Understand and use asynchronous programming with the asyncio library.
# Code:

# import asyncio

# async def hello_world():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")

# asyncio.run(hello_world())

# Problem: Web Scraping with Beautiful Soup
# Description: Extract information from web pages using the Beautiful Soup library for web scraping.
# Code:

# import requests
# from bs4 import BeautifulSoup

# # Make a GET request to a webpage
# response = requests.get('https://example.com')
# html_content = response.content

# # Parse HTML with Beautiful Soup
# soup = BeautifulSoup(html_content, 'html.parser')

# # Extract and print title
# title = soup.title.text
# print(f'Title: {title}')

# Problem: Natural Language Processing with NLTK
# Description: Perform basic natural language processing tasks using the Natural Language Toolkit (NLTK).
# Code:

# import nltk
# from nltk.tokenize import word_tokenize

# nltk.download('punkt')

# # Tokenize a sentence
# sentence = "Natural Language Processing is fascinating!"
# tokens = word_tokenize(sentence)
# print(tokens)


# Problem: Machine Learning with Scikit-Learn
# Description: Build a simple machine learning model using the Scikit-Learn library.
# Code:

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a KNN classifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Make predictions on the test set
predictions = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

# Problem: Asynchronous Programming with asyncio
# - Description: Explore asynchronous programming using the asyncio library in Python.
# - Code:

# import asyncio

# async def hello():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())

# Problem: Data Analysis with Pandas
# - Description: Perform basic data analysis tasks using the Pandas library.
# - Code:

# import pandas as pd

# # Create a DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'San Francisco', 'Los Angeles']}
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)

# # Perform data analysis tasks (e.g., mean, count)
# print(df['Age'].mean())
# print(df['City'].value_counts())

# Problem: Machine Learning with Scikit-Learn
# - Description: Build a simple machine learning model using the Scikit-Learn library.
# - Code:

# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score

# # Load a sample dataset
# from sklearn.datasets import load_iris
# iris = load_iris()
# X, y = iris.data, iris.target

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create a Random Forest classifier
# clf = RandomForestClassifier(n_estimators=100, random_state=42)

# # Train the classifier
# clf.fit(X_train, y_train)

# # Make predictions on the test set
# predictions = clf.predict(X_test)

# # Evaluate accuracy
# accuracy = accuracy_score(y_test, predictions)
# print(f'Accuracy: {accuracy}')

# Problem: Natural Language Processing with NLTK
# - Description: Perform basic natural language processing tasks using the NLTK library.
# - Code:

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist

# # Download NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# # Sample text
# text = "Natural language processing is a subfield of artificial intelligence."

# # Tokenize the text
# words = word_tokenize(text)

# # Remove stopwords
# stop_words = set(stopwords.words('english'))
# filtered_words = [word for word in words if word.lower() not in stop_words]

# # Calculate word frequencies
# freq_dist = FreqDist(filtered_words)
# print(freq_dist.most_common(5))

# Problem: Web Scraping with BeautifulSoup
# - Description: Scrape data from a website using the BeautifulSoup library.
# - Code:

# import requests
# from bs4 import BeautifulSoup

# # Specify the URL
# url = 'https://example.com'

# # Send a GET request
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract data
# title = soup.title.string
# paragraphs = soup.find_all('p')

# # Display the extracted data
# print(f'Title: {title}')
# for i, paragraph in enumerate(paragraphs, 1):
#     print(f'Paragraph {i}: {paragraph.text}')

# Problem: GUI Application with Tkinter
# - Description: Build a simple graphical user interface (GUI) application using the Tkinter library.
# - Code:

import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

# Create the main window
window = tk.Tk()
window.title("Tkinter Example")

# Create widgets
label = tk.Label(window, text="Welcome to Tkinter")
button = tk.Button(window, text="Click me", command=on_button_click)

# Pack widgets
label.pack(pady=10)
button.pack()

# Start the main event loop
window.mainloop()

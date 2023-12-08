# Problem: Web Scraping with BeautifulSoup and Requests

# Description: Write a script to scrape information from a website using BeautifulSoup and Requests.
# Code:

import requests
from bs4 import BeautifulSoup

# Make a request to the website
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract information from the page
title = soup.title.text
paragraphs = soup.find_all("p")

# Print the results
print(f"Title: {title}")
for paragraph in paragraphs:
    print(paragraph.text)

# Problem: Data Visualization with Matplotlib

# Description: Create a visualization using the Matplotlib library.
# Code:

import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
plt.plot(x, y, label="Sine Function")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sine Function Plot")
plt.legend()
plt.show()

# Problem: Natural Language Processing with NLTK

# Description: Perform basic text processing tasks using the Natural Language Toolkit (NLTK).
# Code:
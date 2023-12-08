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
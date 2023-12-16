# Description: Create a simple web scraper using BeautifulSoup and Requests to extract information from a website.
# Code:

# import requests
# from bs4 import BeautifulSoup

# # Specify the URL to scrape
# url = 'https://example.com'

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content with BeautifulSoup
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract information (example: titles)
# titles = soup.find_all('h2')
# for title in titles:
#     print(title.text)

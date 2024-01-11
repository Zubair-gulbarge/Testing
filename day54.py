# Problem: Web Scraping with BeautifulSoup
# - Description: Use BeautifulSoup to scrape data from a website.
# - Code:

# from bs4 import BeautifulSoup
# import requests

# # Make a request to the website
# response = requests.get('https://example.com')

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract information
# title = soup.title.text
# paragraphs = soup.find_all('p')
# for paragraph in paragraphs:
#     print(paragraph.text)

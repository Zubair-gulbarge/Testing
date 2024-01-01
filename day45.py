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

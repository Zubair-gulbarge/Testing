# Problem: Working with APIs (Requests)
# Description: Make API requests and process the JSON response using the Requests library.
# Code:
# import requests

# # Make a GET request to a sample API
# response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# # Print the response content
# print(response.json())

# Problem: Asynchronous Programming with Asyncio
# Description: Implement asynchronous programming using the Asyncio library.
# Code:

# import asyncio

# async def hello_world():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")

# asyncio.run(hello_world())

# Problem: Unit Testing with pytest
# Description: Write and run unit tests for Python code using the pytest library.
# Code (Sample Test):
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

# Problem: Web Scraping with BeautifulSoup
# Description: Scrape data from a website using the BeautifulSoup library.
# Code:

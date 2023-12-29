# Problem: Machine Learning with Scikit-Learn
# Description: Implement a simple machine learning model using Scikit-Learn.
# Code:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate sample data
# np.random.seed(42)
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train a linear regression model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Make predictions on the test set
# predictions = model.predict(X_test)

# # Evaluate the model
# mse = mean_squared_error(y_test, predictions)
# print(f'Mean Squared Error: {mse}')


# Problem: Web Scraping with BeautifulSoup
# Description: Scrape data from a website using the BeautifulSoup library.
# Code:

# import requests
# from bs4 import BeautifulSoup

# # Specify the URL to scrape
# url = 'https://example.com'
# response = requests.get(url)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, 'html.parser')

# # Extract data from the webpage
# title = soup.title.text
# paragraphs = soup.find_all('p')

# print(f'Title: {title}')
# print(f'Paragraphs: {len(paragraphs)}')

# Problem: Asynchronous Web Requests with aiohttp
# Description: Make asynchronous web requests using the aiohttp library.
# Code:

import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = ['https://example.com', 'https://example.org']
    tasks = [fetch(url) for url in urls]
    responses = await asyncio.gather(*tasks)

    for url, response in zip(urls, responses):
        print(f'Content from {url}: {len(response)} characters')

asyncio.run(main())

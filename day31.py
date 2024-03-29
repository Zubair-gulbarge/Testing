# Problem: Asynchronous Programming with Asyncio

# Description: Implement asynchronous programming using the asyncio library.
# Code:

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Problem: Image Processing with Pillow

# Description: Use the Pillow library to perform basic image processing tasks.
# Code:

from PIL import Image, ImageFilter

# Open an image file
original_image = Image.open("input_image.jpg")

# Display image size and format
print(f"Image Size: {original_image.size}, Format: {original_image.format}")

# Convert the image to grayscale
grayscale_image = original_image.convert("L")
grayscale_image.save("grayscale_image.jpg")

# Apply a blur filter to the image
blurred_image = original_image.filter(ImageFilter.BLUR)
blurred_image.save("blurred_image.jpg")

# Problem: Web Scraping with Beautiful Soup

# Description: Use Beautiful Soup to scrape information from a website.
# Code:

import requests
from bs4 import BeautifulSoup

# Make a request to a website
url = "https://example.com"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Extract information from the page
title = soup.title.text
paragraphs = soup.find_all("p")
for paragraph in paragraphs:
    print(paragraph.text)

# Problem: Data Visualization with Matplotlib

# Description: Create visualizations using the Matplotlib library.
# Code:

import matplotlib.pyplot as plt
import numpy as np

# Generate data for plotting
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a line plot
plt.plot(x, y1, label="sin(x)")
plt.plot(x, y2, label="cos(x)")

# Add labels and a legend
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

# Show the plot
plt.show()

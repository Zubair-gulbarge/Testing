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

# Problem: Asynchronous Programming with Asyncio

# Description: Implement asynchronous programming using the asyncio library.
# Code:

# import asyncio

# async def hello_world():
#     print("Hello,")
#     await asyncio.sleep(1)
#     print("World!")

# # Create an event loop and run the coroutine
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello_world())

# Problem: Creating a GUI with Tkinter

# Description: Build a graphical user interface (GUI) using the Tkinter library.
# Code:

import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create a simple Tkinter window
window = tk.Tk()
window.title("Tkinter Example")

# Add a button and label
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

label = tk.Label(window, text="Welcome to Tkinter!")
label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()

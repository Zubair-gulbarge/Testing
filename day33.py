# Problem: Multithreading in Python

# Description: Explore multithreading in Python using the threading module.
# Code:

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

# Problem: Working with SQLite Database

# Description: Use the SQLite database in Python.
# Code:

import sqlite3

# Connect to SQLite database (creates a new file if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        email TEXT
    )
''')

# Insert data into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('john_doe', 'john@example.com'))

# Commit changes and close connection
conn.commit()
conn.close()

# Problem: Web Scraping with BeautifulSoup

# Description: Scrape data from a website using the requests and BeautifulSoup libraries.
# Code:

import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extract data from the HTML
title = soup.title.text
paragraphs = soup.find_all('p')

print(f'Title: {title}')
print('Paragraphs:')
for paragraph in paragraphs:
    print(paragraph.text)

# Problem: Asynchronous Programming with asyncio

# Description: Explore asynchronous programming using the asyncio module.
# Code:
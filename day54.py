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

# Problem: Desktop Automation with PyAutoGUI
# - Description: Automate desktop tasks using the PyAutoGUI library.
# - Code:

import pyautogui
import time

# Open Notepad
pyautogui.press('winleft')
pyautogui.write('notepad')
pyautogui.press('enter')
time.sleep(1)

# Type a message
pyautogui.write('Hello, PyAutoGUI!')

# Save and close
pyautogui.hotkey('ctrl', 's')
time.sleep(1)
pyautogui.write('example.txt')
pyautogui.press('enter')
pyautogui.hotkey('alt', 'f4')

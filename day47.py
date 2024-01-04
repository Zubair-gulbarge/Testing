# Problem: Working with APIs (Requests)
# Description: Make API requests and process the JSON response using the Requests library.
# Code:
import requests

# Make a GET request to a sample API
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Print the response content
print(response.json())

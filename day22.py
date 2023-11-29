# with open("numbers.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file]

# sum_of_numbers = sum(numbers)

# with open("result.txt", "w") as result_file:
#     result_file.write(f"Sum of Numbers: {sum_of_numbers}")

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")
for headline in headlines:
    print(headline.text)

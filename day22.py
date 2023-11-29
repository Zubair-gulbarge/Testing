# with open("numbers.txt", "r") as file:
#     numbers = [int(line.strip()) for line in file]

# sum_of_numbers = sum(numbers)

# with open("result.txt", "w") as result_file:
#     result_file.write(f"Sum of Numbers: {sum_of_numbers}")

# import requests
# from bs4 import BeautifulSoup

# url = "https://example.com"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# headlines = soup.find_all("h2")
# for headline in headlines:
#     print(headline.text)

# import sqlite3

# # Connect to the database
# conn = sqlite3.connect("example.db")
# cursor = conn.cursor()

# # Create a table
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# # Insert data
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 30))

# # Query the database
# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# # Close the connection
# conn.commit()
# conn.close()

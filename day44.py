# Problem: Working with JSON Data
# Description: Parse and manipulate JSON data using the built-in json module.
# Code:

import json

# Sample JSON data
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# Parse JSON
data = json.loads(json_data)

# Accessing values
print(f'Name: {data["name"]}, Age: {data["age"]}, City: {data["city"]}')

# Convert Python object to JSON
new_json_data = json.dumps(data, indent=2)
print(new_json_data)

# Problem: Building a RESTful API with Flask
# Description: Create a simple RESTful API using the Flask framework.
# Code:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)

# Problem: Working with Databases (SQLite)
# Description: Interact with a SQLite database using the sqlite3 module.
# Code:

import sqlite3

# Connect to SQLite database (creates if not exists)
connection = sqlite3.connect('sample.db')

# Create a cursor object
cursor = connection.cursor()

# Create a table
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Insert data
cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John Doe', 25))

# Commit changes and close connection
connection.commit()
connection.close()

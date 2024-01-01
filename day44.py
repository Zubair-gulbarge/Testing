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


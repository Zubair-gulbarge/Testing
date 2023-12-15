# Problem: Data Serialization with JSON

# Description: Serialize and deserialize data using the JSON format.
# Code:

import json

# Python dictionary
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Serialize to JSON
json_data = json.dumps(data, indent=2)

# Print JSON
print(json_data)

# Deserialize JSON
decoded_data = json.loads(json_data)

# Print Python dictionary
print(decoded_data)

# Problem: Sending Email with smtplib

# Description: Send an email using the smtplib library.
# Code:
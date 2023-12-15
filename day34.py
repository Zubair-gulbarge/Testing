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

import smtplib
from email.mime.text import MIMEText

# Sender and recipient email addresses
sender_email = 'your_email@gmail.com'
recipient_email = 'recipient_email@example.com'

# Your email credentials
username = 'your_email@gmail.com'
password = 'your_email_password'

# Email content
subject = 'Test Email'
body = 'This is a test email sent from Python.'

# Create MIMEText object
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_email

# Connect to SMTP server and send email
with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(username, password)
    server.sendmail(sender_email, recipient_email, msg.as_string())


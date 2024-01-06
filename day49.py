# Problem: Working with Databases (SQLite)
# Description: Connect to an SQLite database and perform basic CRUD operations using the sqlite3 module.
# Code:

# import sqlite3

# # Connect to SQLite database
# conn = sqlite3.connect('example.db')

# # Create a table
# conn.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER
#     )
# ''')

# # Insert data
# conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('John Doe', 25))
# conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Jane Smith', 30))

# # Query data
# cursor = conn.execute('SELECT * FROM users')
# for row in cursor.fetchall():
#     print(row)

# # Close connection
# conn.close()

# Problem: Introduction to Flask (Web Framework)
# Description: Create a simple web application using the Flask web framework.
# Code:

# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)

# Problem: Flask - Dynamic Routes and Templates
# Description: Create dynamic routes and use templates in a Flask web application.
# Code:

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Home Page'

# @app.route('/user/<username>')
# def user_profile(username):
#     return render_template('profile.html', username=username)

# if __name__ == '__main__':
#     app.run(debug=True)

# Problem: Django Basics (Web Framework)
# Description: Set up a basic Django project and create a simple web application.
# Code:

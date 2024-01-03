# Problem: Data Visualization with Matplotlib
# Description: Create visualizations using the Matplotlib library.
# Code:
# import matplotlib.pyplot as plt
# import numpy as np

# # Generate data
# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# # Plot the sine wave
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Sine Wave')
# plt.legend()
# plt.show()

# Problem: Web Development with Flask
# Description: Create a simple web application using the Flask web framework.
# Code:
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)

# Problem: GUI Programming with Tkinter
# Description: Develop a basic graphical user interface (GUI) using the Tkinter library.
# Code:

# import tkinter as tk

# def on_button_click():
#     label.config(text="Button Clicked!")

# # Create main window
# window = tk.Tk()
# window.title("Tkinter Example")

# # Create and pack widgets
# button = tk.Button(window, text="Click me!", command=on_button_click)
# button.pack(pady=10)

# label = tk.Label(window, text="Hello, Tkinter!")
# label.pack(pady=10)

# # Run the main loop
# window.mainloop()

# Problem: Working with Databases (SQLite)
# Description: Interact with a SQLite database using the SQLite library in Python.
# Code:

import sqlite3

# Connect to SQLite database (create if not exists)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL queries
cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')

# Insert data
cursor.execute('INSERT INTO users (name) VALUES (?)', ('John Doe',))

# Commit changes and close connection
conn.commit()
conn.close()

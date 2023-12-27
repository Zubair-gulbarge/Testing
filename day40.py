# Problem: GUI Development with Tkinter
# Description: Create a simple GUI application using the Tkinter library.
# Code:

# import tkinter as tk

# def on_button_click():
#     label.config(text="Hello, " + entry.get())

# # Create the main window
# root = tk.Tk()
# root.title("Simple GUI App")

# # Create widgets
# label = tk.Label(root, text="Enter your name:")
# entry = tk.Entry(root)
# button = tk.Button(root, text="Say Hello", command=on_button_click)

# # Arrange widgets
# label.pack()
# entry.pack()
# button.pack()

# # Start the main loop
# root.mainloop()

# Problem: REST API Development with Flask
# Description: Implement a simple REST API using the Flask framework.
# Code:

# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route('/api/hello', methods=['GET'])
# def hello():
#     return jsonify(message="Hello, Flask API!")

# if __name__ == '__main__':
#     app.run(debug=True)

# Problem: Natural Language Processing with NLTK
# Description: Use the Natural Language Toolkit (NLTK) to perform basic NLP tasks.
# Code:

import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

text = "This is a sample sentence for NLP."
tokens = word_tokenize(text)

print("Original Text:", text)
print("Tokenized Words:", tokens)

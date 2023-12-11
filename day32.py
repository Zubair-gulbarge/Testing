# Problem: Working with APIs

# Description: Use the requests library to interact with a public API.
# Code:

# import requests

# # Make a request to a public API (e.g., JSONPlaceholder)
# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)

# # Extract and print JSON data
# data = response.json()
# print(data)

# Problem: Creating a Flask Web Application

# Description: Build a simple web application using the Flask framework.
# Code:

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", message="Hello, Flask!")

# if __name__ == "__main__":
#     app.run(debug=True)

# Problem: Implementing a Class with Inheritance

# Description: Create a class hierarchy with inheritance.
# Code:

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         raise NotImplementedError("Subclasses must implement the speak method")

# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# # Usage
# dog = Dog("Buddy")
# cat = Cat("Whiskers")

# print(dog.speak())  # Output: Buddy says Woof!
# print(cat.speak())  # Output: Whiskers says Meow!


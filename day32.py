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

# Problem: Data Analysis with Pandas

# Description: Analyze data using the Pandas library.
# Code:

# import pandas as pd

# # Create a DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 22],
#         'City': ['New York', 'San Francisco', 'Los Angeles']}
# df = pd.DataFrame(data)

# # Display the DataFrame
# print(df)

# # Perform basic data analysis
# print("Average Age:", df['Age'].mean())
# print("Most common city:", df['City'].mode()[0])

# Problem: Implementing a Decorator

# Description: Create and use a decorator in Python.
# Code:

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

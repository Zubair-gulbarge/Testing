# Problem: REST API Development with Flask
# - Description: Build a simple REST API using the Flask framework.
# - Code:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    return jsonify(message='Hello, Flask API!')

if __name__ == '__main__':
    app.run(debug=True)

# Problem: Database Interaction with SQLAlchemy
# - Description: Connect Python to a relational database using the SQLAlchemy library.
# - Code:

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Connect to the database
engine = create_engine('sqlite:///:memory:')

# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add data
user1 = User(name='John Doe', age=25)
user2 = User(name='Jane Doe', age=30)
session.add_all([user1, user2])
session.commit()

# Query data
users = session.query(User).all()
for user in users:
    print(f'User: {user.name}, Age: {user.age}')

# Problem: Web Development with Django
# - Description: Create a basic web application using the Django framework.
# - Code:

# Install Django: pip install django

# Create a new Django project
django-admin startproject myproject

# Create a new Django app
cd myproject
python manage.py startapp myapp

# Define views in myapp/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")

# Configure URLs in myproject/urls.py
from django.contrib import admin
from django.urls import path
from myapp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

# Run the development server
python manage.py runserver

# Problem: Containerization with Docker
# - Description: Package a Python application into a Docker container.
# - Code:

# Create a Dockerfile:

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]

# Build and run the Docker container:

docker build -t my-python-app .
docker run -p 4000:80 my-python-app

# Problem: Testing with pytest
# - Description: Write and execute tests for a Python application using the pytest framework.
# - Code:

# Install pytest: pip install pytest

# Write test functions in test_myapp.py
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 1 == 2

# Run tests
pytest test_myapp.py


# Problem: Continuous Integration with GitHub Actions
# - Description: Implement continuous integration for a Python project using GitHub Actions.
# - Code:

# Create a GitHub Actions workflow file (.github/workflows/main.yml):

# name: Python CI

# on:
#   push:
#     branches:
#       - main

# jobs:
#   build:
#     runs-on: ubuntu-latest

#     steps:
#     - name: Set up Python
#       uses: actions/setup-python@v2
#       with:
#         python-version: 3.8

#     - name: Install dependencies
#       run: |
#         python -m pip install --upgrade pip
#         pip install -r requirements.txt

#     - name: Run tests
#       run: |
#         pytest

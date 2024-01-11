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

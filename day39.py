# Problem: Asynchronous Programming with Asyncio
# Description: Implement a simple asynchronous program using the asyncio library.
# Code:

# import asyncio

# async def hello_world():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("World")

# asyncio.run(hello_world())

# Problem: Data Visualization with Matplotlib
# Description: Create a visualization using the Matplotlib library.
# Code:

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Sinusoidal Curve')
# plt.show()


# Problem: Working with Databases and SQLAlchemy
# Description: Create a Python script to interact with a SQLite database using SQLAlchemy.
# Code:

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Connect to the database
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add a new user
new_user = User(name='John Doe', age=25)
session.add(new_user)
session.commit()

# Query the database
users = session.query(User).all()
for user in users:
    print(f'User: {user.name}, Age: {user.age}')

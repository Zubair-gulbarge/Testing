# Problem: GUI Application with Tkinter

# Description: Create a graphical user interface (GUI) application using the Tkinter library.
# Code:

# import tkinter as tk

# def on_button_click():
#     label.config(text="Button Clicked!")

# app = tk.Tk()
# app.title("Tkinter GUI App")

# button = tk.Button(app, text="Click me!", command=on_button_click)
# button.pack()

# label = tk.Label(app, text="Welcome to Tkinter!")
# label.pack()

# app.mainloop()

# Problem: Time Series Forecasting with Prophet

# Description: Use the Prophet library for time series forecasting on a given dataset.
# Code:

# from fbprophet import Prophet
# import pandas as pd

# # Load time series data
# data = pd.read_csv("time_series_data.csv")
# data.columns = ["ds", "y"]

# # Create and fit the Prophet model
# model = Prophet()
# model.fit(data)

# # Make future predictions
# future = model.make_future_dataframe(periods=365)
# forecast = model.predict(future)

# # Plot the forecast
# fig = model.plot(forecast)

# Problem: Deep Learning with TensorFlow

# Description: Implement a simple neural network using the TensorFlow library.
# Code:

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Create a simple neural network
model = Sequential()
model.add(Dense(units=64, activation="relu", input_dim=100))
model.add(Dense(units=1, activation="sigmoid"))

# Compile the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Problem: Database Interaction with SQLAlchemy

# Description: Interact with a relational database using the SQLAlchemy library.
# Code:

from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the database model
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

# Create a SQLite database engine
engine = create_engine("sqlite:///:memory:")

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add new user to the database
new_user = User(name="John Doe", age=30)
session.add(new_user)
session.commit()

# Query and print users from the database
users = session.query(User).all()
for user in users:
    print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")

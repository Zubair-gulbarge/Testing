# Problem: Machine Learning with Scikit-Learn

# Description: Implement a simple machine learning model using the Scikit-Learn library.
# Code:

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

# Problem: Flask Web Development

# Description: Create a simple web application using the Flask framework.
# Code:

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", message="Welcome to Flask!")

if __name__ == "__main__":
    app.run(debug=True)

# Problem: Database Interaction with SQLAlchemy

# Description: Use the SQLAlchemy library to interact with a database.
# Code:
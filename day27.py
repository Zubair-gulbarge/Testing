# Problem: Data Analysis with Pandas

# Description: Use the Pandas library to perform data analysis on a given dataset.
# Code:

# import pandas as pd

# # Create a DataFrame from a CSV file
# df = pd.read_csv("sample_data.csv")

# # Perform data analysis tasks (e.g., describe, groupby, plot)
# print(df.describe())
# print(df.groupby("category")["value"].mean())
# df.plot(x="date", y="value", kind="line")

# Problem: Web Development with Flask

# Description: Create a simple web application using the Flask framework.
# Code:

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html", title="Flask Web App")

# if __name__ == "__main__":
#     app.run(debug=True)

# Problem: Image Processing with OpenCV

# Description: Use the OpenCV library to perform basic image processing tasks.
# Code:

import cv2

# Read an image from file
img = cv2.imread("image.jpg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the original and processed images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

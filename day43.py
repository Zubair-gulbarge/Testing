# Problem: Data Visualization with Matplotlib
# Description: Create a simple data visualization using the Matplotlib library.
# Code:

# import matplotlib.pyplot as plt
# import numpy as np

# # Generate sample data
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

# # Plot the data
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sinusoidal Function')
# plt.legend()
# plt.show()

# Problem: Image Processing with OpenCV
# Description: Perform basic image processing tasks using the OpenCV library.
# Code:

# import cv2
# import numpy as np

# # Read an image from file
# image = cv2.imread('path/to/image.jpg')

# # Convert the image to grayscale
# grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian blur
# blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)

# # Display the original and processed images
# cv2.imshow('Original Image', image)
# cv2.imshow('Blurred Image', blurred_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Problem: Unit Testing with unittest
# Description: Write unit tests for a Python function using the unittest framework.
# Code:

import unittest

def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

if __name__ == '__main__':
    unittest.main()

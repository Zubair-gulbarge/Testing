# class Shape:
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2

# # Creating objects of the derived classes
# rectangle = Rectangle(5, 8)
# circle = Circle(4)

# # Calculating and displaying areas
# print(f"Area of the rectangle: {rectangle.area()}")
# print(f"Area of the circle: {circle.area()}")

# class MathOperations:
#     @classmethod
#     def add(cls, x, y):
#         return x + y

#     @staticmethod
#     def multiply(x, y):
#         return x * y

# # Using class methods and static methods
# sum_result = MathOperations.add(3, 7)
# product_result = MathOperations.multiply(4, 5)

# print(f"Sum: {sum_result}")
# print(f"Product: {product_result}")

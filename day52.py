# Problem: Data Visualization with Matplotlib
# - Description: Use Matplotlib to create basic data visualizations such as line charts, bar charts, and scatter plots.
# - Code:

# import matplotlib.pyplot as plt

# # Line Chart
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 7, 12, 8]
# plt.plot(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Chart')
# plt.show()

# # Bar Chart
# categories = ['Category A', 'Category B', 'Category C']
# values = [30, 50, 20]
# plt.bar(categories, values)
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Chart')
# plt.show()

# # Scatter Plot
# x = [1, 2, 3, 4, 5]
# y = [10, 15, 7, 12, 8]
# plt.scatter(x, y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Scatter Plot')
# plt.show()

# Problem: Data Analysis with Pandas
# - Description: Use Pandas to load and analyze a dataset, perform data cleaning, and generate insights.
# - Code:

# import pandas as pd

# # Load dataset
# df = pd.read_csv('example.csv')

# # Display basic information
# print(df.head())
# print(df.describe())

# # Data cleaning
# df.dropna(inplace=True)

# # Analyze data
# average_age = df['Age'].mean()
# print(f'Average Age: {average_age}')

# Problem: Machine Learning with Scikit-Learn
# - Description: Build a simple machine learning model using Scikit-Learn for tasks such as classification or regression.
# - Code:

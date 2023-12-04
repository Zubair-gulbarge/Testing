# Problem: Data Analysis with Pandas

# Description: Use the Pandas library to perform data analysis on a given dataset.
# Code:

import pandas as pd

# Create a DataFrame from a CSV file
df = pd.read_csv("sample_data.csv")

# Perform data analysis tasks (e.g., describe, groupby, plot)
print(df.describe())
print(df.groupby("category")["value"].mean())
df.plot(x="date", y="value", kind="line")

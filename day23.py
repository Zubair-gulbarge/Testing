import pandas as pd

# Load dataset
df = pd.read_csv("example_dataset.csv")

# Filter data
filtered_data = df[df["column_name"] > 50]

# Group by and aggregate
grouped_data = df.groupby("category_column").agg({"numeric_column": "mean"})

# Data visualization
grouped_data.plot(kind="bar")

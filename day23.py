# import pandas as pd

# # Load dataset
# df = pd.read_csv("example_dataset.csv")

# # Filter data
# filtered_data = df[df["column_name"] > 50]

# # Group by and aggregate
# grouped_data = df.groupby("category_column").agg({"numeric_column": "mean"})

# # Data visualization
# grouped_data.plot(kind="bar")

# import asyncio
# import aiohttp

# async def fetch(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     urls = ["https://example.com", "https://example.org", "https://example.net"]
#     tasks = [fetch(url) for url in urls]
#     responses = await asyncio.gather(*tasks)
#     print(responses)

# asyncio.run(main())

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# import pandas as pd

# # Load dataset
# df = pd.read_csv("example_dataset.csv")

# # Prepare data
# X = df[["feature1", "feature2"]]
# y = df["target"]

# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Make predictions
# predictions = model.predict(X_test)

# # Evaluate model
# mse = mean_squared_error(y_test, predictions)
# print(f"Mean Squared Error: {mse}")

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

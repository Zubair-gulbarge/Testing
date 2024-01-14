# Problem: Asynchronous Programming with asyncio
# - Description: Explore asynchronous programming using the asyncio library in Python.
# - Code:

import asyncio

async def hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())

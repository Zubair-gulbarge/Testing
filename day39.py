# Problem: Asynchronous Programming with Asyncio
# Description: Implement a simple asynchronous program using the asyncio library.
# Code:

import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello_world())

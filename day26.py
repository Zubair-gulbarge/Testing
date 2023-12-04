import asyncio

async def example_coroutine():
    print("Start Coroutine")
    await asyncio.sleep(2)
    print("End Coroutine")

asyncio.run(example_coroutine())

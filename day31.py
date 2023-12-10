# Problem: Asynchronous Programming with Asyncio

# Description: Implement asynchronous programming using the asyncio library.
# Code:

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

# Problem: Image Processing with Pillow

# Description: Use the Pillow library to perform basic image processing tasks.
# Code:

from PIL import Image, ImageFilter

# Open an image file
original_image = Image.open("input_image.jpg")

# Display image size and format
print(f"Image Size: {original_image.size}, Format: {original_image.format}")

# Convert the image to grayscale
grayscale_image = original_image.convert("L")
grayscale_image.save("grayscale_image.jpg")

# Apply a blur filter to the image
blurred_image = original_image.filter(ImageFilter.BLUR)
blurred_image.save("blurred_image.jpg")


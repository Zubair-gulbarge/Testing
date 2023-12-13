# Problem: Multithreading in Python

# Description: Explore multithreading in Python using the threading module.
# Code:

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)
        print(letter)

# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

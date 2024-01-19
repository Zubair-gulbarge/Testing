# Problem: Quick Sort

# Description: Implement the quick sort algorithm.
# Code:

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         left = [x for x in arr[1:] if x <= pivot]
#         right = [x for x in arr[1:] if x > pivot]
#         return quick_sort(left) + [pivot] + quick_sort(right)

# Problem: Stack Implementation

# Description: Implement a stack data structure.
# Code:

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

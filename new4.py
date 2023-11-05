# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1  # Target not found

# # Example usage:
# sorted_list = [1, 3, 5, 7, 9, 11, 13]
# target = 7
# result = binary_search(sorted_list, target)
# print(f"Index of {target} is {result}")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.display()

# def longest_common_subsequence(str1, str2):
#     m, n = len(str1), len(str2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]

#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#             else:
#                 dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

#     lcs = []
#     i, j = m, n
#     while i > 0 and j > 0:
#         if str1[i - 1] == str2[j - 1]:
#             lcs.append(str1[i - 1])
#             i -= 1
#             j -= 1
#         elif dp[i - 1][j] > dp[i][j - 1]:
#             i -= 1
#         else:
#             j -= 1

#     return "".join(reversed(lcs))

# # Example usage:
# string1 = "AGGTAB"
# string2 = "GXTXAYB"
# result = longest_common_subsequence(string1, string2)
# print(f"Longest Common Subsequence: {result}")

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def is_empty(self):
#         return len(self.items) == 0

# class Queue:
#     def __init(self):
#         self.items = []

#     def enqueue(self, item):
#         self.items.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.items.pop(0)

#     def is_empty(self):
#         return len(self.items) == 0

# # Example usage:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())

# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(queue.dequeue())


# Using memoization to calculate factorial
# def factorial(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n == 0:
#         return 1
#     result = n * factorial(n - 1, memo)
#     memo[n] = result
#     return result

# # Example usage:
# n = 5
# result = factorial(n)
# print(f"{n}! = {result}")

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# # Example usage:
# array = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(array)
# print("Sorted array:", array)

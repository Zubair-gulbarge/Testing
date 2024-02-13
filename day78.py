# Problem: Implement Depth-First Search (DFS)
# Description: Implement the Depth-First Search algorithm to traverse a graph.
# Code:

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for neighbor in graph[start]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, visited)

# Problem: Implement Breadth-First Search (BFS)
# Description: Implement the Breadth-First Search algorithm to traverse a graph.
# Code:

# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             queue.extend(graph[node] - visited)

# Problem: Check if a String is a Palindrome
# Description: Given a string, determine if it is a palindrome.
# Code:

# def is_palindrome(s):
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]

# Problem: Calculate the Power of a Number
# Description: Implement a function to calculate the power of a number.
# Code:

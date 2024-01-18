# Problem: Binary Tree Traversal (Inorder)

# Description: Implement the inorder traversal of a binary tree.
# Code:

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.value)
#         inorder_traversal(root.right)

# Problem: Hash Table

# Description: Implement a basic hash table.
# Code:

# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def hash_function(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self.hash_function(key)
#         self.table[index].append((key, value))

#     def lookup(self, key):
#         index = self.hash_function(key)
#         for k, v in self.table[index]:
#             if k == key:
#                 return v
#         return None

# Problem: Breadth-First Search (BFS)

# Description: Implement the breadth-first search algorithm on a graph.
# Code:

# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)

#     while queue:
#         current = queue.popleft()
#         print(current)

#         for neighbor in graph[current] - visited:
#             queue.append(neighbor)
#             visited.add(neighbor)

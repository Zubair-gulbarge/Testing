# Problem: Binary Tree Traversal
# Description: Implement in-order, pre-order, and post-order traversal of a binary tree.
# Code:

# class TreeNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# def in_order_traversal(node):
#     if node:
#         in_order_traversal(node.left)
#         print(node.value)
#         in_order_traversal(node.right)

# def pre_order_traversal(node):
#     if node:
#         print(node.value)
#         pre_order_traversal(node.left)
#         pre_order_traversal(node.right)

# def post_order_traversal(node):
#     if node:
#         post_order_traversal(node.left)
#         post_order_traversal(node.right)
#         print(node.value)

# Problem: Graph Representation
# Description: Implement an adjacency list representation of a graph.
# Code:

# from collections import defaultdict

# class Graph:
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def add_edge(self, u, v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

# Problem: Dijkstra's Algorithm
# Description: Implement Dijkstra's algorithm to find the shortest path in a weighted graph.
# Code:

# import heapq

# def dijkstra(graph, start):
#     distances = {node: float('infinity') for node in graph}
#     distances[start] = 0
#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)

#         if current_distance > distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances

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

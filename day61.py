# Problem: Depth-First Search (DFS)

# Description: Implement the depth-first search algorithm on a graph.
# Code:
# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(graph, neighbor, visited)

# Problem: Linked List Implementation

# Description: Implement a basic linked list data structure.
# Code:
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#         else:
#             current = self.head
#             while current.next:
#                 current = current.next
#             current.next = new_node

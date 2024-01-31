# Problem: Implement Breadth-First Search (BFS) on a Graph
# Description: Implement the breadth-first search algorithm on a graph.
# Code:

# from collections import deque
# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])
#     visited.add(start)
#     while queue:
#         node = queue.popleft()
#         print(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.append(neighbor)

# Problem: Check for Bipartite Graph
# Description: Determine whether a given graph is bipartite or not.
# Code:

# def is_bipartite(graph, start):
#     color = {}
#     queue = [start]
#     color[start] = 0
#     while queue:
#         node = queue.pop(0)
#         for neighbor in graph[node]:
#             if neighbor not in color:
#                 color[neighbor] = 1 - color[node]
#                 queue.append(neighbor)
#             elif color[neighbor] == color[node]:
#                 return False
#     return True

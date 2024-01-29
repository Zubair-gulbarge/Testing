# Problem: Depth-First Search (DFS) on a Graph
# Description: Implement the depth-first search algorithm on a graph.
# Code:

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     print(start)
#     for next_node in graph[start] - visited:
#         dfs(graph, next_node, visited)
#     return visited

# Problem: Topological Sorting of a Directed Acyclic Graph (DAG)
# Description: Implement the topological sorting algorithm on a directed acyclic graph.
# Code:

# def topological_sort(graph):
#     visited = set()
#     stack = []
#     def dfs(node):
#         visited.add(node)
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 dfs(neighbor)
#         stack.append(node)
#     for node in graph:
#         if node not in visited:
#             dfs(node)
#     return stack[::-1]

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

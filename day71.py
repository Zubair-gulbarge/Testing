# Problem: Detect a Cycle in a Directed Graph
# Description: Implement an algorithm to detect cycles in a directed graph.
# Code:

# def is_cyclic(graph):
#     visited = set()
#     rec_stack = set()
#     def dfs(node):
#         if node in rec_stack:
#             return True
#         if node in visited:
#             return False
#         visited.add(node)
#         rec_stack.add(node)
#         for neighbor in graph[node]:
#             if dfs(neighbor):
#                 return True
#         rec_stack.remove(node)
#         return False
#     for node in graph:
#         if dfs(node):
#             return True
#     return False

# Problem: Find the Strongly Connected Components (SCCs) in a Directed Graph
# Description: Implement an algorithm to find the strongly connected components in a directed graph.
# Code:

# def dfs(graph, node, stack, visited):
#     visited.add(node)
#     for neighbor in graph[node]:
#         if neighbor not in visited:
#             dfs(graph, neighbor, stack, visited)
#     stack.append(node)
# def transpose_graph(graph):
#     transposed = {node: set() for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             transposed[neighbor].add(node)
#     return transposed
# def find_scc(graph):
#     stack = []
#     visited = set()
#     for node in graph:
#         if node not in visited:
#             dfs(graph, node, stack, visited)
#     transposed = transpose_graph(graph)
#     visited.clear()
#     sccs = []
#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             scc = set()
#             dfs(transposed, node, scc, visited)
#             sccs.append(scc)
#     return sccs

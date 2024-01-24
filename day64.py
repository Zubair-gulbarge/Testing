# Problem: Depth-First Search (DFS)
# Description: Implement the depth-first search algorithm on a graph.
# Code:

def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

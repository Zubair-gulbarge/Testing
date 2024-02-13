# Problem: Implement Depth-First Search (DFS)
# Description: Implement the Depth-First Search algorithm to traverse a graph.
# Code:

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

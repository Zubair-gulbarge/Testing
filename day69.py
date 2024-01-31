# Problem: Implement Breadth-First Search (BFS) on a Graph
# Description: Implement the breadth-first search algorithm on a graph.
# Code:

from collections import deque
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

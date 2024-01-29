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

# Problem: Find the Shortest Path in a Weighted Graph using Dijkstra's Algorithm
# Description: Implement Dijkstra's algorithm to find the shortest path in a weighted graph.
# Code:

# import heapq
# def dijkstra(graph, start):
#     distances = {vertex: float('infinity') for vertex in graph}
#     distances[start] = 0
#     pq = [(0, start)]
#     while pq:
#         current_distance, current_vertex = heapq.heappop(pq)
#         if current_distance > distances[current_vertex]:
#             continue
#         for neighbor, weight in graph[current_vertex].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(pq, (distance, neighbor))
#     return distances

# Problem: Implement a Priority Queue in Python
# Description: Implement a priority queue data structure in Python.
# Code:

class PriorityQueue:
    def __init__(self):
        self.heap = []
    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))
    def pop(self):
        return heapq.heappop(self.heap)[1]

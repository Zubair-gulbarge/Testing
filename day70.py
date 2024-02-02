# Problem: Topological Sorting of a Directed Acyclic Graph (DAG)
# Description: Implement topological sorting to find the linear ordering of vertices in a directed acyclic graph.
# Code:

# def topological_sort(graph):
#     in_degree = {node: 0 for node in graph}
#     for node in graph:
#         for neighbor in graph[node]:
#             in_degree[neighbor] += 1
#     queue = [node for node in graph if in_degree[node] == 0]
#     topo_order = []
#     while queue:
#         node = queue.pop(0)
#         topo_order.append(node)
#         for neighbor in graph[node]:
#             in_degree[neighbor] -= 1
#             if in_degree[neighbor] == 0:
#                 queue.append(neighbor)
#     return topo_order

# Problem: Find the Shortest Path in a Weighted Graph using Dijkstra's Algorithm
# Description: Implement Dijkstra's algorithm to find the shortest path in a weighted graph.
# Code:

# import heapq
# def dijkstra(graph, start):
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0
#     queue = [(0, start)]
#     while queue:
#         current_distance, current_node = heapq.heappop(queue)
#         if current_distance > distances[current_node]:
#             continue
#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(queue, (distance, neighbor))
#     return distances

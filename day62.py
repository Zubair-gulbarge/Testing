# Problem: Dijkstra's Algorithm

# Description: Implement Dijkstra's algorithm for finding the shortest path in a weighted graph.
# Code:
# import heapq

# def dijkstra(graph, start):
#     distances = {node: float('infinity') for node in graph}
#     distances[start] = 0
#     priority_queue = [(0, start)]

#     while priority_queue:
#         current_distance, current_node = heapq.heappop(priority_queue)

#         if current_distance > distances[current_node]:
#             continue

#         for neighbor, weight in graph[current_node].items():
#             distance = current_distance + weight

#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 heapq.heappush(priority_queue, (distance, neighbor))

#     return distances

# Problem: Quick Sort
# Description: Implement the quicksort algorithm.
# Code:

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# Problem: Breadth-First Search (BFS)
# Description: Implement the breadth-first search algorithm on a graph.
# Code:
# from collections import deque

# def bfs(graph, start):
#     visited = set()
#     queue = deque([start])

#     while queue:
#         node = queue.popleft()
#         if node not in visited:
#             print(node)
#             visited.add(node)
#             queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

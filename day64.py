# Problem: Depth-First Search (DFS)
# Description: Implement the depth-first search algorithm on a graph.
# Code:

# def dfs(graph, node, visited):
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbor in graph[node]:
#             dfs(graph, neighbor, visited)

# Problem: Binary Search
# Description: Implement the binary search algorithm on a sorted list.
# Code:

# def binary_search(arr, target):
#     low, high = 0, len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

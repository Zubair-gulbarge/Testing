# Problem: Find the Maximum Subarray Sum
# Description: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# Code:

# def max_subarray(nums):
#     max_sum = float('-inf')
#     current_sum = 0
#     for num in nums:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# Problem: Implement Depth First Search (DFS)
# Description: Implement the depth first search algorithm to traverse a graph.
# Code:

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

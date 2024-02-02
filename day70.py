# Problem: Topological Sorting of a Directed Acyclic Graph (DAG)
# Description: Implement topological sorting to find the linear ordering of vertices in a directed acyclic graph.
# Code:

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    queue = [node for node in graph if in_degree[node] == 0]
    topo_order = []
    while queue:
        node = queue.pop(0)
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return topo_order

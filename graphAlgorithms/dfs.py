import math
import time

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(f"Visiting: {vertex}")
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    return visited

graph = {
    0: {1, 2},
    1: {2},
    2: {3},
    3: {1, 2}
}

# Starting the DFS from vertex 0
visited_order = dfs_recursive(graph, 0)
print("DFS Visited Order:", visited_order)







def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(f"Visiting: {vertex}")
            visited.add(vertex)
            # Adds the neighbors in reverse order to visit them in the expected order
            stack.extend(reversed(list(graph[vertex] - visited)))
    return visited

# Starting the DFS from vertex 0
visited_order = dfs_iterative(graph, 0)
print("DFS Visited Order:", visited_order)

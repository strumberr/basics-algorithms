import math
import time
def bfsAlgorithm(graph, start):
    visited = []
    queue = [start]
    while queue:
        print(f"Queue: {queue}")
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(graph[vertex] - set(visited))
        time.sleep(1)
    return visited
graph = {
    0: {1, 2},
    1: {2},
    2: {3},
    3: {1, 2}
}
print(bfsAlgorithm(graph, 0))
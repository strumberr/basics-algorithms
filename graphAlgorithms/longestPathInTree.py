import math
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = {i: [] for i in range(vertices)}

    def saveGraph(self, file):
        G = nx.Graph()
        for u in range(self.vertices):
            for v in self.adjList[u]:
                G.add_edge(u, v)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.savefig(file)

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def bfs(self, start):
        """Performs BFS and returns the last visited node and its distance from the start."""
        visited = [False] * self.vertices
        queue = [(start, 0)]  # Each element is a tuple (node, distance_from_start)
        visited[start] = True
        last = (start, 0)

        while queue:
            current, dist = queue.pop(0)
            last = (current, dist)

            for neighbor in self.adjList[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, dist + 1))

        return last

    def findLongestPathLength(self):
        # First BFS to find one endpoint of the longest path
        node, _ = self.bfs(0)
        # Second BFS from the first BFS's farthest node to find the longest path
        _, longestPathLength = self.bfs(node)
        return longestPathLength

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(0, 2)
g.saveGraph('graphAlgorithms/results/graph.png')

longestPathLength = g.findLongestPathLength()
print(f"The length of the longest path is: {longestPathLength}")

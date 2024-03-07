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
        
        print(self.adjList)
    
    def isBipartite(self):
        visited = [False] * self.vertices
        color = [-1] * self.vertices
        
        print(visited)
        print(color)

        def dfs(v, c):
            
            visited[v] = True
            color[v] = c
            
            for u in self.adjList[v]:
                
                
                if color[u] == c:
                    return False
                
                if not visited[u] and not dfs(u, 1 - c):
                    return False
                        
            return True
        

        for v in range(self.vertices):
            
            if not visited[v]:
                
                if not dfs(v, 0):

                    return False
        
        
        print(color)
        return True
    

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)
g.addEdge(0, 2)
g.saveGraph('graphAlgorithms/results/graph.png')
print(g.isBipartite())


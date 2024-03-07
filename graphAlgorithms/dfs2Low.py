

def dfs(x, p, visited, G, low, layer, n):
    visited[x] = True
    low[x] = layer[x]  # Assuming 'layer[x]' is already defined before calling dfs

    for w in G[x]:
        if not visited[w]:
            layer[w] = layer[x] + 1
            dfs(w, x, visited, G, low, layer, n)  # Pass 'x' as the parent of 'w'
            low[x] = min(low[x], low[w])  # Update low-link value for 'x'
        elif w != p:
            # This is a back-edge, update the low-link value of 'x'
            low[x] = min(low[x], layer[w])
            
    
    return visited  # Return the visited array after the DFS traversal

# Example of how to call this function:
n = 5  # Number of nodes in the graph
visited = [False] * n
G = [[] for _ in range(n)]  # Adjacency list representation of the graph
low = [float('inf')] * n  # Initialize low-link values
layer = [0] * n  # Initialize layers (depth) of each node in the DFS tree

# Assuming 'G' is populated and 'n' is defined
print(dfs(0, -1, visited, G, low, layer, n))
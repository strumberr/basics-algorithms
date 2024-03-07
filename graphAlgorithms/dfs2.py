

def dfs(x, p):
    
    visited = [False] * n
    G = [[] for i in range(n)]
    
    visited[x] = True
    low[v] = layer[v]
    
    
    for w in G[x]:
        if not visited[w]:
            layer[w] = layer[x] + 1
            dfs(w, v)
            low[v] = min(low[v], low[w])
        else:
            if w != p:
                low[v] = min(low[v], layer[w])
            
    return visited


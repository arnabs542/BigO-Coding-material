#Bellman ford algorithm
INF = 10e9

def BellmanFord(source,graph,dist):
    dist[source] = 0
    for node in range(n):
        for edge in graph:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
    for edge in graph:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True


if __name__ == '__main__':

    n, m = map(int,input().split())
    graph = []
    dist = [INF for i in range(n+5)]
    path = [-1 for i in range(n+5)]
    for j in range(m):
        u, v, w = map(int,input().split())
        graph.append((u,v,-w))
        graph.append((v,u,-w))
    s = 1
    res = BellmanFord(s,graph,dist)

    print(path)
    print(dist[5])

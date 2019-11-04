#Bellman-Ford algorithm
INF = int(1e9)

class Triad:
    source = 0
    target = 0
    weight = 0
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

def BellmanFord(source,graph,dist):
    dist[source] = 0
    for i in range(1,n):
        for j in graph:
            u = j.source
            v = j.target
            w = j.weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                
    for i in graph:
        u = i.source
        v = i.target
        w = i.weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True

if __name__ == '__main__':
    testcase = int(input())
   
    for cs in range(testcase):
        n, m = map(int,input().split())
        graph = []
        dist = [INF for i in range(n+5)]
        #path = [-1 for i in range(n+5)]
        for i in range(m):
            u, v, w = map(int,input().split())
            graph.append(Triad(u,v,w))
        s = 0
        res = BellmanFord(s, graph, dist)

        
        if res == False:
            print('possible')
        else:
            print('not possible')
    

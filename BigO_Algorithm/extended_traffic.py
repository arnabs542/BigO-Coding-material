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
    print(dist)        
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
        print()
        n = int(input())
        junc_list = list(map(int,input().split()))
        m = int(input())
        
        graph = []
        dist = [INF for i in range(n+5)]
        #path = [-1 for i in range(n+5)]
        for i in range(m):
            u, v = map(int,input().split())
            w = (junc_list[v-1] - junc_list[u-1])**3
            
            graph.append(Triad(u,v,w))

        for item in graph:
            print(item.source, item.target, item.weight)
        s = 0
        res = BellmanFord(s, graph, dist)
        #print(dist)
    

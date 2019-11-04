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
    dist[source] = 1.0
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
    while True:
        n = int(input())
        if n == -1:
            break
        graph = []
        dist = [INF for i in range(n+5)]
        cost_list = []
        connection = list()
        lst = list()
        for node in range(1,n,1):
            lst.append(list(map(int,input().split())))
            cost_list.append(lst[0])

        for item in cost_list:
            print(item)
        for item in lst:
            print(item)

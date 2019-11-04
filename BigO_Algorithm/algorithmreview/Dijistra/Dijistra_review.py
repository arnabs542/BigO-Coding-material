#Dijistra review
import queue
MAX = 100
INF = int(1e9)
class Node:
    dist = 0
    id = 0
    def __init__(self,id,dist):
        self.dist = dist
        self.id = id
    def __lt__(self,other):
        return self.dist <= other.dist

def Dijistra(s,graph,dist):
    pq = queue.PriorityQueue()
    pq.put(Node(s,0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        node = top.id
        d = top.dist
        for neighbor in graph[node]:
            if d + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = d + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))
                path[neighbor.id] = node
if __name__ == '__main__':
    V, E = map(int,input().split())
    graph = [[] for i in range(V+5)]
    dist = [INF for i in range(V+5)]
    path = [-1 for i in range(V+5)]
    for i in range(E):
        u, v, cost = map(int,input().split())
        graph[u].append(Node(v,cost))
    s = 0
    t = 4
    Dijistra(s, graph, dist)
    ans = dist[t]
    for i in range(V+1):
        print(path[i], end = ' ')
    print()
    print(ans)

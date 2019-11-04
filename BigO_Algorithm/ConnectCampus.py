#Minimum spanning tree
import queue
INF = 1e9
class Node:
    dist = 0
    id = 0
    def __init__(self,id,dist):
        self.dist = dist
        self.id = id
    def __lt__(self,other):
        return self.dist <= other.dist
def printMST():
    ans = 0
    for i in range(1,n+1,1):
        print(path[i])
        if path[i] == -1:
            continue
        ans += dist[i]
        print("{0} - {1}: {2}".format(path[i],i,dist[i]))
    #print("Weight of MST: {0}".format(ans))
    print(ans)

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src,0))
    dist[src] = 0
    while pq.empty() == False:
        for item in pq.queue:
            print((item.id, item.dist), end = '')
        print()
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v,w))
                path[v] = u
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        lst_city = []
        graph = [[] for i in range(n+5)]
        dist = [INF for i in range(n+5)]
        path = [-1 for i in range(n+5)]
        visited = [False for i in range(n+5)]
        for i in range(n):
            x, y = map(int,input().split())
            lst_city.append((x,y))
            
        m = int(input())
        connection = []
        for j in range(m):
            u, v = map(int,input().split())
            connection.append((u,v))
            
        for i in range(n):
            for j in range(n):
                if j == i:
                    continue
                distance = ((lst_city[j][0]-lst_city[i][0])**2 + (lst_city[j][1]-lst_city[i][1])**2)**(1/2)
                #u, v, w = map(int,input().split())
                graph[i].append(Node(j,distance))
                graph[j].append(Node(i,distance))
            #Prim(1)
            #printMST()
        for i in range(n):
            for item in graph[i]:
                print(i, item.id, item.dist)

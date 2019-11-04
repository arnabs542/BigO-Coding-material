#Prim minimum spanning tree review
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
    for i in range(n+1):
        if path[i] == -1:
            continue
        ans += dist[i]
        #print('{0} - {1}: {2}'.format(path[i],i,dist[i]))
    return ans
    #print('Weight of MST: {0}'.format(ans))

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src,0))
    dist[src] = 0
    while pq.empty() == False:
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
    case = int(input())
    result = []
    print()
    for cs in range(case):
        print()
        tmp = input()
        n = int(input())
        graph = [[] for i in range(n+1)]
        dist = [INF for i in range(n+1)]
        path = [-1 for i in range(n+1)]
        visited = [False for i in range(n+1)]
        lst = []
        for i in range(n):
            x, y = map(float,input().split())
            lst.append((x,y))
        #print(lst)
        for i in range(n-1):
            for j in range(i+1,n,1):
                distance = ((lst[j][0] - lst[i][0])**2 + (lst[j][1] - lst[i][1])**2)**(1/2)
                #print(i,j,distance)
                graph[i].append(Node(j,distance))
                graph[j].append(Node(i,distance))
        Prim(0)
        result.append(round(printMST(),2))

    for res in result:
        print()
        print(res)

#Implementation of BFS:
from queue import Queue 

MAX = 100 
V = None 
E = None 
visited = [False]*MAX #Initialize explored territory as empty 
path = [0]*MAX #Initialize path 
graph = [[] for i in range(MAX)] #Initialize graph as 2D arrays 


#Breadth First Search implementation
def BFS(src):
    for i in range(V):
        visited[i] = False 
        path[i] = -1 
    q = Queue()
    visited[src] = True 
    q.put(src)

    while q.empty() == False:
        v = q.get()
        for w in graph[v]:
            if visited[w] == False:
                visited[w] = True 
                q.put(w)
                path[w] = v 


#find the path from s to f
def printPath(s,f,path):
    b = []
    if f == s:
        print(f)
        return 

    if path[f] == -1:
        print('No path')
        return 
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break 
    for i in range(len(b)-1,-1,-1):
        print(b[i], end=' ')


if __name__ == '__main__':
    V, E = map(int,input().split())
    for i in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    s = 1
    d = 5 
    BFS(s)
    printPath(s,d,path)
    print()

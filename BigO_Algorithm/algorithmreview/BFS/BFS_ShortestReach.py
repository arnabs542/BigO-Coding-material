#BFS implementation
from queue import Queue

MAX = 100
V = None
E = None


def BFS(src):
    for i in range(1,V+5,1):
        visited[i] = False
        path[i] = -1
    q = Queue()
    visited[src]= True
    q.put(src)

    while q.empty() == False:
        src = q.get()
        for v in graph[src]:
            if visited[v] == False:
                visited[v] = True
                q.put(v)
                path[v] = src

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
        print(b[i], end = ' ')

def countPath(s,d,path):
    count = 0
    b = []
    if path[d] == -1:
        return -1
    while True:
        b.append(d)
        d = path[d]
        count += 1
        if d == s:
            b.append(s)
            return count
            break

if __name__ == '__main__':
    q = int(input())
    for case in range(q):
       
        V, E = map(int,input().split())
        visited = [False]*(V+5)
        path = [0]*(V+5)
        graph = [[] for i in range(V+5)]
        result = []
        for i in range(E):
            u, v = map(int,input().split())
            graph[u].append(v)
            graph[v].append(u)
        s = int(input())
        BFS(s)
       
        for i in range(1,V+1,1):
            d = i
            if d == s:
                continue
            tmp = countPath(s,d,path)
            result.append(tmp)

        weight = 6
        for i in result:
            if i == -1:
                tmp = -1
            else:
                tmp = weight * i
            print(tmp, end = ' ')
        print()
        
    

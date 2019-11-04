#Shortest path using BFS:
#https://www.hackerrank.com/challenges/bfsshortreach/problem
from queue import Queue 


MAX = 100
V = None 
E = None 

visited = [False]*MAX 
path = [0]*MAX 
graph = [[] for i in range(MAX)]
level = [-1]*MAX 

def printPath(src):
    for v in range(0,V+1):
        # print(f'source: {src} and v: {v}')
        b = []
        if v != src:
            if path[v] == -1:
                print(-1, end=' ')
                continue 
            
            while True:
                b.append(v)
                v = path[v]
                if v == src:
                    #b.append(src)
                    break 
            print(6*len(b), end =' ')
    


def BFS(src):
    for i in range(0,V+1):
        visited[i] = False 
        path[i] = -1 
        level[i] = -1

    visited[src] = True
    q = Queue()
    q.put(src)
    level[src] = 0

    while not q.empty():
        v = q.get()
        for w in graph[v]:
            if visited[w] == False:
                visited[w] = True 
                q.put(w)
                path[w] = v 
                level[w] = level[v] + 1

    # print('visited: ', visited)
    # print('path: ', path)



if __name__ == '__main__':
    V, E = map(int,input().split())
    for i in range(E):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)


    # for i in range(1,V+1):
    #     print(graph[i])

    s = 0
    BFS(s)
    for node in range(V):
        print(level[node])
    # printPath(s)
    # print()
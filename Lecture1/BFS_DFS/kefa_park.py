#Kefa and Park: http://codeforces.com/problemset/problem/580/C
import queue 

MAX = 100
graph = [[] for _ in range(MAX)]
visited = [False]*MAX
path = [-1]*MAX 

def BFS(src, dest):
    result = False 
    for i in range(n+1):
        visited[i] = False 
        path[i] = 0 
    q = qeuue.Queue()
    q.put(src)
    visited[src] = True 

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True 
                q.put(v)
                path[v] = u    

    return result 


if __name__ == '__main__':
    n, m = map(int,input().split())
    ls = list(map(int,input().split()))
    for _ in range(n-1):
        u, v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    s = 1 
    leaves = []
    count = 0 
   
    for i in range(n+1):
        if (len(graph[i]) == 1):
            leaves.append(i)
    
    print(ls)
    print(leaves)
    for d in leaves:
        if BFS(s,d):
            count += 1
    print(count)
        
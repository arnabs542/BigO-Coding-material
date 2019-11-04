#Floyd-Warshall
MAX = 100
INF = int(1e9)
def printPath(s,t):
    b = []
    while s!= t:
        b.append(t)
        t = path[s][t]
    b.append(s)
    for i in range(len(b)-1,-1,-1):
        print(b[i],end=' ' if i > 0 else '\n')

def FloydWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] == False and i != j and dist[i][k] + dist[k][j] == 2:
                    dist[i][j] = True
                    path[i][j] = 1
                if i == 0 and j == 4:
                    print(dist[i][j])
if __name__ == '__main__':
    n = int(input())
    graph = [[None for i in range(n)] for j in range(n)]
    dist = [[None for i in range(n)] for j in range(n)]
    path = [[None for i in range(n)] for j in range(n)]
    for i in range(n):
        line = list(input())
        for j in range(n):
            if line[j] == 'Y':
                graph[i][j] = True
            else:
                graph[i][j] = False
    for item in graph:
        print(item)
    print()
    FloydWarshall(graph,dist)
    #for item in dist:
    #    print(item)
    #print()
    #for item in path:
    #    print(item)
    #s, t = 0, 4
    #printPath(s,t)
    #print(dist[s][t])

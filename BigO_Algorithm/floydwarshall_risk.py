INF = int(1e9)

def FloydWarshall(graph,dist):
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] == None and i != j:
                dist[i][j] = INF
            else:
                dist[i][j] = graph[i][j]

        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                if i == 17 and j == 18:
                    print(k,dist[i][j], dist[i][k], dist[k][j])

if __name__ == '__main__':
    n = 20
    graph = [[None for i in range(n)] for j in range(n)]
    dist = [[INF for i in range(n)] for j in range(n)]
    for i in range(1,n,1):
        lst = list(map(int,input().split()))
        for num in range(lst[0]):
            graph[i-1][lst[1 + num]-1] = 1
            graph[lst[1 + num]-1][i-1] = 1
    FloydWarshall(graph,dist)
    print(dist[0][19])
    print(dist[7][19])
    print(dist[14][15])
    print(dist[10][3])
    print(dist[6][12])
    print(dist[1][15])

        

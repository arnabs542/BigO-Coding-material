INF = float(1e9)

def FloydWarshall(graph,dist):
    max_distance = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = round(graph[i][k] + graph[k][j],4)

    for i in range(n):
        for j in range(n):
            if graph[i][j] > max_distance and graph[i][j] < INF:
                max_distance = graph[i][j]
            elif graph[i][j] == INF:
                max_distance = -1
                break

    
    return max_distance

if __name__ == '__main__':
    testcase = int(input())
    for cs in range(testcase):
        n = int(input())
        graph = [[None for i in range(n+5)] for j in range(n+5)]
        dist = [[INF for i in range(n+5)] for j in range(n+5)]
        town = []
        for i in range(n):
            x, y = map(int,input().split())
            town.append((x,y))

        for i in range(n):
            for j in range(n):
                if i == j:
                    graph[i][j] = 0
                else:
                    dist = round(((town[j][0] - town[i][0])**2 + (town[j][1] - town[i][1])**2)**(1/2.0),4)
                    if dist > 10.0:
                        graph[i][j] = INF
                    else:
                        graph[i][j] = dist

        
        print('Case #%d: ' %(cs+1))
        res = FloydWarshall(graph,dist)
        
        if res > 0:
            print(res)
        else:
            print('Send Kurdy')
        
        print()
  

        

#Traveling cost
#Dijistra algorithm
import queue
MAX = 100
INF = int(1e9)


def Dijistra(s,graph,dist):
    pq = queue.PriorityQueue()
    pq.put((s,0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        node = top[0]
        d = top[1]
        for neighbor in graph[node]:
            if d + neighbor[1] < dist[neighbor[0]]:
                dist[neighbor[0]] = d + neighbor[1]
                pq.put((neighbor[0],dist[neighbor[0]]))
                path[neighbor[0]] = node

if __name__ == '__main__':
    testcase = int(input())
    result = list()
    n = 10000
    while(testcase > 0):
        graph = [[] for i in range(n+5)]
        city = int(input())
        list_city = list()
        u = 0
        for i in range(city):
            list_city.append(input())
            u += 1
            connection = int(input())
            for j in range(connection):
                v, cost = map(int,input().split())
                graph[u].append((v,cost))
        number_path = int(input())
        path_list = list()
        for p in range(number_path):
            city1, city2 = input().split()
            path_list.append((city1, city2))
        for item in path_list:
            s = list_city.index(item[0]) + 1
            d = list_city.index(item[1]) + 1
            dist = [INF for i in range(n+5)]
            path = [-1 for i in range(n+5)]
            Dijistra(s,graph,dist)
            ans = dist[d]
            result.append(ans)
        testcase = testcase - 1
        print()
    for item in result:
        print(item)

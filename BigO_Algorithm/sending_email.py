#Sending email
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
    n = 50000
    while(testcase > 0):
        graph = [[] for i in range(n+5)]
        n, m, s, d = map(int,input().split())
        for i in range(m):
            u, v, cost = map(int,input().split())
            graph[u].append((v,cost))
            graph[v].append((u,cost))

        dist = [INF for i in range(n+5)]
        path = [-1 for i in range(n+5)]
        Dijistra(s,graph,dist)
        ans = dist[d]
        result.append(ans)
        testcase = testcase - 1

    #print(result)
    for i in range(len(result)):
        if result[i] == INF:
            print('Case ' + '#%d: ' %i + 'unreachable')
        else:
            print('Case ' + '#%d: %d' % (i,result[i]) )

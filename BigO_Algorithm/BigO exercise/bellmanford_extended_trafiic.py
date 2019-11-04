#Bellman ford algorithm
#Extended traffic
INF = 10e9

def BellmanFord(source,graph,dist):
    dist[source] = 0
    for node in range(n):
        for edge in graph:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            print(u,v,w)
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u
                #print(dist)

    for edge in graph:
        u = edge[0]
        v = edge[1]
        w = edge[2]
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True
            

if __name__ == '__main__':
    testcase = int(input())
    for cs in range(testcase):
        print()
        n = int(input())
        result = []
        graph = []
        dist = [INF for i in range(n+5)]
        path = [-1 for i in range(n+5)]
        junc_list = list(map(int,input().split()))
        m = int(input())
        for edge in range(m):
            u,v = map(int,input().split())
            w = (junc_list[v-1] - junc_list[u-1])**3
            graph.append((u,v,w))
        #print(graph)
        query = int(input())
        query_list = []
        for q in range(query):
            query_list.append(int(input()))
        print(dist)
        s = 1
        res = BellmanFord(s,graph,dist)
        for q in query_list:
            result.append(dist[q])
        print(result)
            
    

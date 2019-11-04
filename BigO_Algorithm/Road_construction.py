#Minimum spanning tree
import queue
INF = 1e9
class Node:
    dist = 0
    id = 0
    def __init__(self,id,dist):
        self.dist = dist
        self.id = id
    def __lt__(self,other):
        return self.dist <= other.dist
def printMST():
    ans = 0
    for i in range(n):
        #print(path[i])
        if path[i] == -1 and i == 0:
            continue
        elif path[i] == -1 and i != 0:
            return -1
        ans += dist[i]
        #print("{0} - {1}: {2}".format(path[i],i,dist[i]))
    #print("Weight of MST: {0}".format(ans))
    return ans

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src,0))
    dist[src] = 0
    while pq.empty() == False:
        #for item in pq.queue:
            #print((item.id, item.dist), end = '')
        #print()
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v,w))
                path[v] = u
if __name__ == '__main__':
    testcase = int(input())
    for case in range(testcase):
        print()
        m = int(input())
        list_city = []
        lst_input = []
       
        for i in range(m):
            u, v, w = input().split()
            if u not in list_city:
                list_city.append(u)
            if v not in list_city:
                list_city.append(v)
            lst_input.append((u,v,w))

        n = len(list_city)
        graph = [[] for i in range(n+1)]
        dist = [INF for i in range(n+1)]
        path = [-1 for i in range(n+1)]
        visited = [False for i in range(n+1)]
        for i in range(len(lst_input)):
            graph[list_city.index(lst_input[i][0])].append(Node(list_city.index(lst_input[i][1]),int(lst_input[i][2])))
            graph[list_city.index(lst_input[i][1])].append(Node(list_city.index(lst_input[i][0]),int(lst_input[i][2])))
                                                           
        Prim(0)
        result = printMST()
        if result > 0:
            print('Case %d: %d' % (case+1,result))
        else:
            print('Case %d: Impossible' % (case+1))

#Dhoom4 problem hackerrank
import queue 

dist = [-1]*100005

def BFS(start, lock):
    q = queue.Queue()
    q.put(start)
    dist[start] = 0
    # count = 0
    while not q.empty():
        # count += 1
        u = q.get()
        if u == lock:
            return dist[u]
        for i in range(n):
            v = (u * ls[i]) % 100000
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)
    # print(count)
    return -1


if __name__ == '__main__':
    s, l = map(int,input().split())
    n = int(input()) 
    ls = list(map(int,input().split()))

    print(BFS(s, l))
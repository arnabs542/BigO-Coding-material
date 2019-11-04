#That is your queue
import queue
P, C = map(int,input().split())
lst = list()
for i in range(C):
    lst.append(input().split())

q = queue.Queue()
population = min(P,C)
for i in range(1,population + 1,1):
    q.put(i)
    
for item in lst:
    print(item)



#Where is the marble
import bisect
case = 0
while True:
    case += 1
    n, q = map(int,input().split())
    #input()
    if n == 0 and q == 0:
        break
    lst = []
    query = []
    for i in range(n):
        lst.append(int(input()))
    #input()
    for j in range(q):
        query.append(int(input()))

    lst.sort()
    
    pos = []
    for i in range(q):
        temp = bisect.bisect_left(lst,query[i],0,n)
        #print(temp)
        if temp > n-1 or query[i] != lst[temp]:
            temp = -1
        pos.append(temp + 1)

    print('CASE# %d:' % case)
    for i in range(q):
        if pos[i] != 0:
            print('%d found at %d' % (query[i], pos[i]))
        else:
            print('%d not found' % query[i])
            

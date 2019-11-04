#Disjoint Set Union
def findSet(u):
    while u!= parent[u]:
        u = parent[u]
    return u

def unionSet(u,v):
    up = findSet(u)
    vp = findSet(v)
    parent[vp] = up

if __name__ == '__main__':
    result = []
    while True:
        n, m = map(int,input().split())
        if n == 0 and m == 0:
            break
        parent = [i for i in range(n+1)]

        for i in range(m):
            u, v = map(int,input().split())
            tmp1 = findSet(u)
            tmp2 = findSet(v)
            if tmp1 != tmp2:
                unionSet(u,v)
        count = 0
        for i in range(n+1):
            if i != 0 and i == parent[i]:
                count += 1

        result.append(count)

    for i in range(len(result)):
        print('Case {0}: {1}'.format(i+1,result[i]))

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
    q = int(input())
    parent = [i for i in range(20)]
    result = []
    for i in range(q):
        u, v, c = map(int,input().split())
        if c == 1:
            unionSet(u,v)
        else:
            tmp1 = findSet(u)
            tmp2 = findSet(v)
            result.append(int(tmp1 == tmp2))

    for res in result:
        print(res)

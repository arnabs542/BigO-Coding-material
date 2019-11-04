#Megacity
n, s = map(int,input().split())
d = dict()
for i in range(n):
    x, y, p = map(int,input().split())
    distance = round((x**2 + y**2)**(1/2),7)
    if distance not in d:
        d[distance] = p
    else:
        d[distance] = d[distance] + p

radius = 0
lst = list(d.items())
lst.sort()

population = s
for i in range(len(lst)):
    radius = lst[i][0]
    population = population + lst[i][1]
    if population >= 1000000:
        print(radius)
        break

if population < 1000000:
    print(-1)
        

    

#Bear and Game
n = int(input())
lst = list(map(int,input().split()))
t0 = 0
tend = 90
for t in lst:
    if t > t0 + 15:

        break
    else:
        t0 = t

if t0 + 15 < tend:
    print(t0 + 15)
else:
    print(tend)


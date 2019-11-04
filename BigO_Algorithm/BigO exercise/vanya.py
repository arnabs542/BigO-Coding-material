#Vanya and Fence
n, h = map(int,input().split())
lst = list(map(int,input().split()))
count = 0
for item in lst:
    if item <= h:
        count = count + 1
    else:
        count = count + 2
print(count)

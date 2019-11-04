#Berland and fashion
n = int(input())
lst = list(map(int,input().split()))
count = 0
for item in lst:
    if item == 0:
        count += 1

if (len(lst) == 1 and lst[0] == 0) or count > 1 or (len(lst) > 1 and count == 0):
    print('NO')
else:
    print('YES')


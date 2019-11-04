#Geroge problem
n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
i = 0
j = 0
count = 0
result = n
while (j < m or i < n):
    if b[j] >= a[i]:
        i += 1
        j += 1
        count += 1
    else:
        j += 1
    if ((j == m) and (i < n)) or (i == n):
        break

result = n - count
print(result)


#Panoramix prediction
def isPrime(n):
    for j in range(2,int(n**(1/2)+1),1):
        if n % j == 0:
            return False
    return True


n, m = map(int,input().split())
flag = True
for i in range(n+1,m+1,1):
    if i < m and isPrime(i):
        #print(i)
        flag = False
        break
if flag and isPrime(m):
    print('YES')
else:
    print('NO')

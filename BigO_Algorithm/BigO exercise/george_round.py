#George and round
n, m = map(int,input().split())
n_list = list(map(int,input().split()))
m_list = list(map(int,input().split()))
result = n
i = 0
j = 0
while i < n and j < m:
   if n_list[i] > m_list[j]:
       j += 1
   else:
        i += 1
        j += 1
        result = result - 1
            

print(result)
        

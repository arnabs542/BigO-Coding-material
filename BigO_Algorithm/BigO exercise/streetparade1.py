#Street parade
while True:
    n = int(input())
    if n == 0:
        break
    lst = list(map(int,input().split()))
    st = []
    count = 1
    i = 0
    final = []
    flag = True
    while i < n:
        if len(st) == 0:
            if lst[i] != count:
                st.append(lst[i])
                
            else:
                final.append(lst[i])
                count += 1
        else:
            if st[-1] == count:
                final.append(st.pop())
                count += 1
            elif lst[i] != count:
                st.append(lst[i])
            elif lst[i] == count:
                final.append(lst[i])
                
        i += 1
    while len(st) > 0:
        final.append(st.pop())
    print(final)
    for j in range(len(final)-1):
        if final[j] > final[j+1]:
            flag = False
            break
        
    if flag:
        print('yes')
    else:
        print('no')
    
    
            
        
                
        
            
        
        
    

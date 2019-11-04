#Street Parade
n = 1
while (n >0):
    n = int(input())
    result = list()
    flag = True
    if n == 0:
        break
    lst = list(map(int,input().split()))
    st = []
    final = []
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            if len(st) == 0 or lst[i] < st[-1]:
                st.append(lst[i])
            else: 
                while len(st) > 0 and lst[i] > st[-1]:
                    final.append(st.pop())
                st.append(lst[i])
        else:
            if len(st) > 0 and lst[i] > st[-1]:
                while len(st) > 0 and lst[i] > st[-1]:
                    final.append(st.pop())
                st.append(lst[i])
            else:
                final.append(lst[i])
        #print('final', final)
        #print('st',st)
    final.append(lst[i+1])
    while len(st) > 0:
        final.append(st.pop())

    for i in range(len(final)-1):
        if final[i] > final[i+1]:
            flag = False

    if flag:
        print('yes')
    else:
        print('no')
  

        
        
        
        
            
            
            

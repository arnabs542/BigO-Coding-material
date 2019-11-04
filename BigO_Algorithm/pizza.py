#Pizza pair
import bisect
testcase = int(input())
for i in range(testcase):
    n, m = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    pair = []
    count = 0
    for i in range(n):
        if i in pair:
            continue
        else:
            first_val = lst[i]
            new_lst = lst[i+1:]
            print(new_lst)
            second_val = m - first_val
            pos = bisect.bisect_left(new_lst, second_val,0,len(new_lst))
            print(pos)
            if pos > len(new_lst):
                continue
            else:
                pair.append(pos)
                count += 1
    print(count)
            
        
            
    

#Pizza friends
import bisect

testcase = int(input())
for case in range(testcase):
    n, m = map(int,input().split())
    lst = list(map(int,input().split()))
    lst.sort()
    #print(lst)
    count = 0
    check = []
    for i in range(n-1):
        first_val = lst[i]
        if first_val not in check:
            second_val = m - first_val
            pos = bisect.bisect_left(lst[i+1:], second_val, 0, len(lst[i+1:]))
            #print(pos, len(lst[i+1:]))
            if pos < len(lst[i+1:]) and lst[pos+i+1] == second_val:
                count += 1
                check.append(second_val)
            #print(first_val, second_val,pos)

    print(count)


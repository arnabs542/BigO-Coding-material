#GBUS count
testcase = int(input())

#result = []
for case in range(testcase):
    if case != 0:
        dump = input()
    n = int(input())
    list_input = list(map(int,input().split()))
    list_bus = []
    i = 0
    while i < 2*n:
        list_bus.append((list_input[i],list_input[i+1]))
        i += 2
    p = int(input())
    
    result = []
    for j in range(p):
        city = int(input())
        count = 0
        for bus in list_bus:
            #print(city, bus)
            if city >= bus[0] and city <= bus[1]:
                count += 1
        result.append(count)
    
    print('Case #{}: '.format(case + 1), end = '')
    for res in result:
        print(res, end =' ')
    print()
    


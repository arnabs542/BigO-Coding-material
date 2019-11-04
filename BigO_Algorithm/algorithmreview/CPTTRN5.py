#CPTTRN5
testcase = int(input())
flag = True
count = 0
for case in range(testcase):
    row, col, s = map(int,input().split())
    for r in range(row*(s+1) + 1):
        for c in range(col*(s+1) + 1):
            if c % 3 == 0 or r % 3 == 0:
                print('*', end = '')
            elif (r+c) % 2 == 0 and flag:
                print('\\', end = '')
                count += 1
                if count == s:
                    count = 0
                    flag = False
            elif (r+c) % 2 == 0 and not flag:
                print('/', end = '')
                count += 1
                if count == s:
                    count = 0
                    flag = True
                
            else:
                print('.',end='')
        print()

#CPTTRN3 - Character Patterns 3
        
testcase = int(input())
for case in range(testcase):
    row, col = map(int,input().split())
    for r in range(row*3+1):
        for c in range(col*3+1):
            if c%3 == 0 or r % 3 == 0:
                print('*',end='')
            else:
                print('.',end='')
        print()
        
        
            
            

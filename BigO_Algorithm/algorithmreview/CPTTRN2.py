#CPTTRN2 - Character Patterns 2
testcase = int(input())
for case in range(testcase):
    col, row = map(int,input().split())
    for c in range(col):
        for r in range(row):
            if c == 0 or c == col -1 or r == 0 or r == row - 1:
                print('*',end='')
            else:
                print('.',end='')
        print()
    print()

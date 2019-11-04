#CPTTRN1 - Character Patterns 1
testcase = int(input())
for case in range(testcase):
    col, row = map(int,input().split())
    for c in range(col):
        for r in range(row):
            if (r + c) % 2 == 0:
                print('*',end='')
            else:
                print('.',end='')
        print()
    print()

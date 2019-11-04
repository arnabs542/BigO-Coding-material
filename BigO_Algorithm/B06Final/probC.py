#Problem C
def swap(a,b):
    temp = a
    a = b
    b = temp
n = int(input())
lst = list(map(int,input().split()))
task = []
task1 = []
task2 = []
for i in range(n):
    task.append((lst[i],i+1))
task.sort()
for i in range(n):
    task1.append(task[i])
    task2.append(task[i])
count = 1
for i in range(n-1):
    #print(task[i], task[i+1])
    if task[i][0] == task[i+1][0]:
        if count == 1:
            task1[i], task1[i+1] = task1[i+1], task1[i]
            #print(task1)
            count += 1
        elif count == 2:
            task2[i], task2[i+1] = task2[i+1], task2[i]
            count += 1
            break
if count != 3:
    print('NO')
else:
    print('YES')
    for i in range(n):
        print(task[i][1], end = ' ')
    print()
    for i in range(n):
        print(task1[i][1], end = ' ')
    print()
    for i in range(n):
        print(task2[i][1], end = ' ')
    print()

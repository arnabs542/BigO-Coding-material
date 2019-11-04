#Hackerrank grading challenge
def nextMul5(x):
    return (x//5 + 1)*5

n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))

new_ls = []
for item in ls:
    if nextMul5(item) - item < 3 and item >= 38:
        new_ls.append(nextMul5(item))
    else:
        new_ls.append(item)

for i in new_ls:
    print(i)
    
            
        
    

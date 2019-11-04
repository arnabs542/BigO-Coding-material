#Eleven chooses names
n = int(input())
Fib_arr = [0 for i in range(n+5)]
result = []
def Fib(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 1
    else:
        return Fib_arr[i-1] + Fib_arr[i-2]

for i in range(n+5):
    Fib_arr[i] = Fib(i)

for num in range(1,n+1,1):
    if num in Fib_arr:
        result.append('O')
    else:
        result.append('o')

print(''.join(result))
    
    


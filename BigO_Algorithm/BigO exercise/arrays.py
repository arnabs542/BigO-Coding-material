#Arrays
na, nb = map(int,input().split())
k, m = map(int,input().split())
array_a = list(map(int,input().split()))
array_b = list(map(int,input().split()))

size_a = len(array_a)
size_b = len(array_b)
flag = True
sub_a = array_a[0:k]
sub_b = array_b[size_b - m:size_b]
if sub_a[len(sub_a)-1] >= sub_b[0]:
   flag = False
if flag:
   print('YES')
else:
   print('NO')

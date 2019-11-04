#Global and local inversions
A = [2,1,0]
local_inversion = 0
global_inversion = 0
gl = 0
for j in range(len(A)):
    if A[j] > j:
        gl += A[j] - j
for i in range(len(A)-1):
    if A[i] > A[i+1]:
        local_inversion += 1
        global_inversion += 1
print(global_inversion, gl, local_inversion)
if global_inversion == gl:
    print(True)
else:
    print(False)

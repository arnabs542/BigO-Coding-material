#Nicolas and permutation
n = int(input())
lst = list(map(int,input().split()))
min_index = lst.index(min(lst))
max_index = lst.index(max(lst))

delta_left = min(min_index, max_index)
delta_right = min(len(lst)-1 - min_index,len(lst)-1 - max_index)
result = 0
if delta_left < delta_right:
    result = delta_right + abs(max_index - min_index)
elif delta_left > delta_right:
    result = delta_left + abs(max_index - min_index)
else:
    result = delta_left + abs(max_index - min_index)

print(result)

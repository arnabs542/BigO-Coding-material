#Segments
segment = int(input())
lst = list()
for i in range(segment):
    lst.append(list(map(int,input().split())))

left_segment = list()
right_segment = list()
for item in lst:
    left_segment.append(item[0])
    right_segment.append(item[1])

left_segment.sort()
right_segment.sort()
min_left = left_segment[0]
max_right = right_segment[len(right_segment)-1]
count = 0
for item in lst:
    count += 1
    if item[0] == min_left and item[1] == max_right:
        print(count)
        break
    if count == len(lst):
        print(-1)
    

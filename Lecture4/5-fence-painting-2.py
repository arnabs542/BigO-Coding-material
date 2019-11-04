# def calculateStroke(arr, left, right, painted_height):
# 	print(arr, left, right, painted_height)
# 	if left == right:
# 		return 0
#
# 	min_height = min(arr[left: right+1])
# 	stroke = min_height - painted_height
# 	left_stroke = 0
# 	right_stroke = 0
# 	for i in range(right-left):
# 		if arr[i] == min_height:
# 			stroke += calculateStroke(arr, left, i, min_height)
# 			stroke += calculateStroke(arr, i, right, min_height)
#
# 	return min(stroke, right - left + 1)
#
#
# if __name__ == '__main__':
# 	n = int(input())
# 	arr = list(map(int, input().split()))
#
# 	print(calculateStroke(arr, 0, n-1, 0))



import sys
sys.setrecursionlimit(1000000)

def calculateStroke(arr, left, right, painted_height):
  #print(arr, left, right, painted_height)
  if left >= right:
    return 0

  min_height = min(arr[left: right])
  min_pos = arr[left: right].index(min_height) + left
  #print('Min pos:', min_pos)
  stroke = min_height - painted_height




  stroke += calculateStroke(arr, left, min_pos, min_height)
  stroke += calculateStroke(arr, min_pos + 1, right, min_height)


	#left = 0, right = 2
  return min(stroke, right - left)



#2 2 1 2 1
#calculateStroke(arr, 0, 4, 0)
#2


if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().split()))

	print(calculateStroke(arr, 0, n, 0))

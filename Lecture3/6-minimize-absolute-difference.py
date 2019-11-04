import heapq 
import copy



def minimize_absolute_difference(ins, value_arr, index_arr, pos):
	global min_value
	global result 
	#print(value_arr)
	if pos == 4:
		temp_min = abs(value_arr[0]/value_arr[1] - value_arr[2]/value_arr[3])
		if temp_min < min_value:
			print('Case less', index_arr, temp_min)	
			result = copy.copy(index_arr)
			min_value = temp_min
			#print(result)
		
		elif temp_min == min_value:
			print('Case equal', index_arr, temp_min)
			if index_arr < result:
				result = copy.copy(index_arr)
			

		return
	
	for i in range(len(ins)):
		if i not in index_arr:
			value_arr[pos] = ins[i]
			index_arr[pos] = i 
			minimize_absolute_difference(ins, value_arr, index_arr, pos+1)
			value_arr[pos] = None
			index_arr[pos] = None


if __name__ == '__main__':
	ins = list(map(int, input().split()))
	value_arr = [None] * 4
	index_arr = [None] * 4
	result = [100000, 100000, 100000, 100000]
	min_value = 100000 
	minimize_absolute_difference(ins, value_arr, index_arr, 0)
	print(*result)

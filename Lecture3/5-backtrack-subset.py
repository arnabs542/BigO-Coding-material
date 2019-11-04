def back_track(arr, powerset, subset, pos):
	powerset.append(subset)
	print('subset: ', subset)	
	for i in range(pos, len(arr)):
		#print(i, arr[i])
		subset.append(arr[i])
		back_track(arr, powerset, subset, i+1)
		subset.pop()
		#print('Remove: ', subset.pop())

	return powerset

if __name__ == '__main__':
	arr = [1,2,3]
	subset = []
	powerset = []
	powerset = back_track(arr, powerset, subset, 0)
	print(len(powerset))
	for sub_set in powerset:
		print(sub_set)

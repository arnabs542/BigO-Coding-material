def find_missing_number(arr):
	#arr: 1 2 3 4 5 6 7 8 9
	n = len(arr)
	max_val = max(arr)
	total_sum = max_val*(max_val+1)/2
	arr_sum = 0
	for e in arr:
		arr_sum += e

	return total_sum - arr_sum
	

def find_missing_number_xor(arr):
	n = len(arr)
	max_val = max(arr)

	total_sum_xor = 1
	for i in range(2, max_val + 1):
		total_sum_xor = total_sum_xor ^ i

	sum_xor = 0
	for element in arr:
		sum_xor = sum_xor ^ element
		
	return sum_xor ^ total_sum_xor	



if __name__ == '__main__':
	arr = [1,2,3,4,6,7,8,9]
	element = find_missing_number(arr)
	print(element)

	element_xor = find_missing_number_xor(arr)
	print(element_xor)

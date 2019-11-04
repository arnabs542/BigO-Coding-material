def generate_sub_array(input_arr, start, end):
	if end == len(input_array):
		return None	

	elif start > end:
		end += 1
		return generate_sub_array(input_arr, 0, end)
	
	elif start <= end:
		generate_sub_array(input_arr, start + 1, end)
		return input_arr[start: end+1]	
		print(start, end, input_arr[start:end+1])
	


if __name__ == '__main__':
	input_array = list(map(int, input().split()))
	output_array = generate_sub_array(input_array, 0, 0)
	print(output_array)

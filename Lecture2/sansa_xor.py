def generate_sub_array(arr):
	n = len(arr)	
	result = []
	# O(n^2)
	for num in range(1, n+1):
		for i in range(n - num + 1):
			result.append(arr[i:i+num])
	
	output_cnt = {} 
	for res in result:
		for num in res:
			try:
				output_cnt[num] += 1 
			except:
				output_cnt[num] = 1

	return output_cnt


def generate_sub_array_v1(arr):
	n = len(arr)	
	num = [0] * n # [0, 0, 0, 0]
	xor_result = 0
	for num_set_bit in range(1, n+1): 
		num[0: num_set_bit]	 = [1] * num_set_bit
		binary_num = int(''.join(str(x) for x in num), 2)
		for j in range(n - num_set_bit + 1):
			xor_result ^= binary_num
			binary_num = binary_num >> 1
			

	print(xor_result, bin(xor_result))
	num_ls = list(bin(xor_result))	
	output = 0 
	for i in range(n):
		print(num_ls[i], arr[i])
		if num_ls[i+2] == '1':
			output = output ^ arr[i]

	print(output)
	exit(1)
	return num


if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n = int(input())
		arr = list(map(int, input().split()))
		#output_cnt = generate_sub_array(arr)

		temp = generate_sub_array_v1(arr)
		xor_result = 0
		for k, v in output_cnt.items():
			if v % 2 != 0:
				xor_result = xor_result ^ k

		print(xor_result)

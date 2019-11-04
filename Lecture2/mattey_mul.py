def refactor(num):
	n = num
	bin_ls = []
	while n > 0:
		temp = n % 2
		n = n >> 1
		bin_ls.append(temp)

	bin_ls.reverse()
	return bin_ls


def shift_mul(num1, num2):
	"""
	refactor num2 to sum of power of 2

	"""
	result = ''
	bin_ls = refactor(num2)
	n = len(bin_ls) - 1
	for i in range(len(bin_ls)):
		if bin_ls[i] == 1: #can get the bit directly 
			shift_string = '(' + str(num1) + '<<' + str(n-i) + ')'
			if result == '':
				result += shift_string
			else:
				result += ' + ' + shift_string
			
		
	
	print(result)


if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n, m = map(int, input().split())
		shift_mul(n,m)
		#print(shift_mul(n, m))

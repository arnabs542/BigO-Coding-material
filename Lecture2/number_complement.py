#https://leetcode.com/problems/number-complement/
def findComplement(num):
	result = num 
	x = 1
	while x <= num:
		#print(x)
		result = result ^ x
		x = x << 1

	return result

input_num = int(input())
print(findComplement(input_num)) #expect 2

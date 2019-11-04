#https://leetcode.com/problems/single-number/
def singleNumber(nums):
	xor_sum = nums[0]
	for i in range(1, len(nums)):
		xor_sum = xor_sum ^ nums[i]


	return xor_sum


ls = list(map(int, input().split()))
print(singleNumber(ls))
	

"""

0 1
1 1 
--> 2

1 0 0 0 0 1 
1 0 0 0 1 0
0 0 0 0 1 1 
--> 2


1 0 1 
1 0 0
--> 2

xor : 0 0 1
or :  1 0 1
--> (1) xor ^ or 1 0 0 
--> (1) | or: 1 0 1

1 1 0 0 1 
1 1 1 0 0 

--> 1
xor: 0 0 1 0 1
or : 1 1 1 0 1 
"""
#pseudocode:
#- Find all possible subsets of dishes that total num of set bits == num of dishes  

def subset_dishes(num_dishes):
	"""
	dishes: [1,2,3,4]
	output: all possible non-empty subsets 
	"""
	bit_len = num_dishes #for example: [0, 0, 0, 0] --> 4
	bit_num = 0
	max_bit_num = 2**bit_len - 1 
	subset = []
	while bit_num < max_bit_num: #O(2^k)
		bit_num += 1
		temp_ls = list(bin(bit_num))[2:]
		if len(temp_ls) < k:
			padding = ['0'] * (k - len(temp_ls))
			temp_ls = padding + temp_ls
		subset.append(temp_ls)


	return subset	


def transpose(in_mat):
	out_mat = []	
	for i in range(len(in_mat[0])):
		new_row = []
		for j in range(len(in_mat)):
			new_row.append(in_mat[j][i])
		out_mat.append(new_row)

	return out_mat


def count_set_bit(ls):
	count = 0
	for i in range(len(ls)):
		if ls[i] == '1':
			count += 1

	return count


if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n, k = map(int, input().split())
		friend_ls = [] 
		for i in range(n): # collect friends' favorited dishes
			friend_ls.append(list(map(int, input())))

		# transpose friend list: O(n*k)
		friend_ls_transpose = transpose(friend_ls)

		subset = subset_dishes(k)
		num_dish = []
		for s in subset:
			possible = []
			for i in range(k):
				if s[i] == '1':
					if sum(friend_ls_transpose[i]) == n:
						#print('Num dish 1')
						num_dish.append(1) 
						break
					else:
						possible.append(friend_ls_transpose[i])
			#count = 0
			temp = 0
			for poss in possible:
				#print('Possible: ', possible)
				temp = temp | int(''.join(str(x) for x in poss),2)
				#count =+ 1
				if count_set_bit(list(bin(temp))[2:]) == n:
					#print('Enough dishes')	
					num_dish.append(len(possible))

		print(min(num_dish))

# Samu birthday
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

    # print(friend_ls_transpose)
    new_list = []
    for item in friend_ls_transpose:
      new_list.append(int(''.join(str(x) for x in item),2))

    #print(new_list)

    #subset = subset_dishes(k) # O(2^k * k)

    bit_len = k  #for example: [0, 0, 0, 0] --> 4
    bit_num = 0
    max_bit_num = 2**bit_len - 1
    subset = []
    num_dish = []
    while bit_num < max_bit_num: #O(2^k)
      bit_num += 1
      temp_ls = list(bin(bit_num))[2:]
      if len(temp_ls) < k:
        padding = ['0'] * (k - len(temp_ls))
        temp_ls = padding + temp_ls
		  #subset.append(temp_ls)

      #print('Temp list: ',temp_ls)

    #for s in subset:
      possible = []
      temp = 0
      count_dish = 0
      for i in range(k):

        if temp_ls[i] == '1':
          if sum(friend_ls_transpose[i]) == n:
            #print('Num dish 1')
            num_dish.append(1)
            break
          else:
            count_dish += 1
            temp = temp | new_list[i]
            #possible.append(new_list[i])
            if count_set_bit(list(bin(temp))[2:]) == n:
              #print(count_dish)
              num_dish.append(count_dish)
              #print(num_dish)
      #temp = 0
      #for poss in possible:
				#print('Possible: ', possible)
      #  temp = temp | poss

      #  if count_set_bit(list(bin(temp))[2:]) == n:
					#print('Enough dishes')
      #    num_dish.append(len(possible))

    print(min(num_dish))

def A_n_k(a, n, k, depth, used, curr, ans):
	"""
	depth: start from 0, or the depth of the search
	used: track what items are in partial solution from the set n
	curr: the current partial solution
	ans: collect all the valid solutions
	"""
	print('depth:', depth)
	if depth == k:
		print('Append curr to ans')
		print('Append curr: ', curr)
		ans.append(curr[::])
		return  

	for i in range(n):
		print('i:',i)
		if not used[i]:
			curr.append(a[i])
			used[i] = True 
			print('curr: ', curr)
			A_n_k(a, n, k, depth+1, used, curr, ans)

			curr.pop()
			print('backtrack: ', curr)
			used[i] = False

	return 


def should_swap(ls, start, end):
	for i in range(start, end):
		if ls[i] == ls[end]:
			return False

	return True


def distinct_permutation(ls, start, end):
	"""
	prints all the permutations of a list 
	Input: a list, start and end indices
	Output: print all permutations
	"""
	#print('Interim list: ', ls)
	if (start >= end):
		print(ls)
		return 
	for i in range(start, end):
		check = should_swap(ls, start, i)
		if check == True:
			
		#print('i: {} start {} end {}'.format(i, start, end))
		#print('swap {} and {}'.format(ls[start], ls[i]))
		
			ls[start], ls[i] = ls[i], ls[start] #swapping
		
			distinct_permutation(ls, start+1, end)
		
		#print('backtrack {} and {}'.format(ls[start], ls[i]))
			ls[start], ls[i] = ls[i], ls[start] #backtracking


distinct_permutation(list('aabb'), 0, 4)
#a = [1,2,3]
#n = len(a)
#ans = [[None]]
#used = [False] * n
#ans = []
#A_n_k(a, n, n, 0, used, [], ans)
#print(ans)

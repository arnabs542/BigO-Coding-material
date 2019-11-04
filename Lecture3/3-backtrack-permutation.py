def back_track_permutation(result, characters, pos):
	
	if pos == 4:
		total_result.append(result)
		print(result)
		return 

	for c in characters:
		if c not in result:
			result[pos] = c
			back_track_permutation(result, characters, pos+1)
			result[pos] = None

total_result = []
if __name__ == '__main__':
	string = 'abcd'
	result = [None] * 4
	back_track_permutation(result, string, 0)
	print(len(total_result))

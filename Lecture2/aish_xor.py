def processing(arr, cnt, l, r):

	#can be replaced by cnt[r] - cnt[l - 1]::
	if arr[l] == 0:
		num_unset = cnt[r] - cnt[l] + 1
	else:
		num_unset = cnt[r] - cnt[l]
	
	num_element = l - r + 1
	num_one = num_element - num_unset
	if num_one % 2 == 0:
		return 0, num_unset
	else:
		return 1, num_unset



if __name__ == '__main__':
	n = int(input())
	ls = list(map(int, input().split()))
	q = int(input())
	cnt = [0] * n # represents number of 0 encountered until position i
	for i in range(len(ls)):
		if ls[i] == 0:
			cnt[i] += 1
	

	for i in range(n):
		cnt[i] += cnt[i-1]

	for i in range(q):
		l, r = map(int, input().split())
		xor_val, num_unset_bits = processing(ls, cnt, l-1, r-1)
		print(xor_val, num_unset_bits)

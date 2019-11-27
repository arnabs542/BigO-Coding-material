


if __name__ == '__main__':
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	i = 0
	current_sum = 0
	done = False

	while k > 0:

		if arr[i] < 0:
			k -= 1
			arr[i] *= (-1)
			current_sum += arr[i]

		elif arr[i] == 0:
			k = 0
			current_sum += sum(arr[i:])
			done = True
		else: #arr[i] > 0
			if k % 2 == 0:
				k = 0
				current_sum += sum(arr[i:])
				done = True
			else: #k odd
				k = 0
				current_sum = max(current_sum - arr[i-1] + arr[i] - arr[i-1],
								  current_sum - arr[i])

		if i < n-1 and k > 0:
			i += 1
		else:
			break


	if k > 0:
		if k % 2 != 0:
			current_sum -= arr[n-1]
			arr[n-1] *= (-1)
			current_sum += arr[n-1]

	if i <= n-1 and not done:
		current_sum += sum(arr[i+1:])

	print(current_sum)

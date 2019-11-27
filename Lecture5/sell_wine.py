

if __name__ == '__main__':
	while True
		n = int(input())
		if n == 0:
			break
		arr = list(map(int, input().split()))
		buy_arr = [0 for _ in range(n)]
		sell_arr = [0 for _ in range(n)]
		for i in range(n):
			if arr[i] > 0:
				buy_arr[i] = arr[i]
			else:
				sell_arr[i] = arr[i]

		total_work = 0
		i = 0
		j = 0
		while True:
			if buy_arr[i] > 0:
				

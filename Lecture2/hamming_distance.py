
def hamming_distance(num1, num2):
	bin1 = num1
	bin2 = num2
	count = 0
	while (bin1 != 0) or (bin2 != 0):
		last_bit = (bin1 & 1) ^ (bin2 & 1)
		if last_bit:
			count += 1
		bin1 = bin1 >> 1
		bin2 = bin2 >> 1

	return count


def hamming_distance_v2(num1, num2):
	count = 0
	n = num1 ^ num2
	while n > 0:
		count += (n & 1)
		n = n >> 1
	return count 

if __name__ == '__main__':
	n1, n2 = map(int, input().split())
	print(hamming_distance_v2(n1, n2))

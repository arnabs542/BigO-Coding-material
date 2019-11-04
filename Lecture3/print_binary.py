
def printBinary(n, prefix=""):
	"""
	print all the binary with n digits
	"""
	print('printBinary(n = {} prefix = {})'.format(n, prefix))
	if n == 0:
		print(prefix)
	else:
		printBinary(n-1, prefix + "0")
		printBinary(n-1, prefix + "1")


printBinary(3)

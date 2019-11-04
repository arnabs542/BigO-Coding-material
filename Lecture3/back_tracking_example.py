N = 4
board = [[0] * N for i in range(N)]


def printSolution():
	for i in range(N):
		for j in range(N):
			print(board[i][j], end=' ')
		print()
	print()


def check(board, row, col):
	# Check vertical
	for i in range(row):
		if board[i][col]:
			return False 

	# Check main diagonal
	i = row
	j = col 
	while i >= 0 and j >= 0:
		if board[i][j]:
			return False 

		i -= 1
		j -= 1

	# Check secondary diagonal:
	i = row
	j = col 
	while j < N and i >= 0:
		if board[i][j]:
			return False 

		i -= 1
		j += 1

	return True 


def NQueen(board, row):
	if row == N:
		printSolution()
		return True 

	for j in range(N): # go thru columns 
		if check(board, row, j) == True:
			board[row][j] = 1
			NQueen(board, row + 1)
			board[row][j] = 0
	
	return False 


if __name__ == '__main__':
	NQueen(board, 0)

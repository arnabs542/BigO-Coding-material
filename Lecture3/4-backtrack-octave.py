#https://www.spoj.com/problems/UCI2009D/
def check_valid(maze, row, col):
	if (row < 0 or row >= n or col >= n or col < 0 or maze[row][col] == '.'):
		#print('invalid col {} row {}'.format(col, row))
		return False

	return True


def back_track(maze, visited, octave, col, row):
	#print('Interim octave: ', octave)
	#print(visited)
	if len(octave) == 8:
		print(octave)	
		return

	if check_valid(maze, row, col) and not visited[row][col]:
		visited[row][col] = True
		octave.append(col + n*row)
		for i in range(4):
			col = col + dx[i]
			row = row + dy[i]
			#print('goto: i {} col {} row {}'.format(i, col, row))
			back_track(maze, visited, octave, col, row)
			col = col - dx[i]
			row = row - dy[i]

		visited[row][col] = False
		octave.pop()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
if __name__ == '__main__':
	testcase = int(input())
	for case in range(testcase):
		n = int(input())
		maze = [[] for i in range(n)]
		octave = [] 
		for j in range(n):
			maze[j] = list(input())

		print(maze)
		visited = [[False for i in range(n)] for j in range(n)]
		back_track(maze, visited, octave, 0, 0)


